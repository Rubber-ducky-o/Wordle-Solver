from .data_splitting import Data
import math
import sys

GRAY = "rgb(58, 58, 60)"
YELLOW = "rgb(181, 159, 59)"
GREEN = "rgb(83, 141, 78)"

class Solver:
    def __init__(self):
        self.data = Data()
        self.count = 0
        self.win = False
        self.game_over = False
        self.guess_count = 0
        # LETTER | VALUE | POSITION
        self.feedback = [['',0,0],
                         ['',0,1],
                         ['',0,2],
                         ['',0,3],
                         ['',0,4]]


    def word_choice(self) -> str:

        if self.count == 0:
            self.count += 1
            return self.determinized_start()

        else:

            next_word = self.best_move()


            if self.data.debug:

                print(f"Possible Words Left: {len(self.data.possible_words)}")
                print(f"NEXT BEST MOVE IS: {next_word}")

            self.data.possible_words.pop(next_word)

            for index, char in enumerate(next_word):
                self.feedback[index][0] = char

            return next_word


    def determinized_start(self) -> str:
        word = self.data.randomized_start()

        for index, char in enumerate(word):
            self.feedback[index][0] = char


        if self.data.debug:
            print(f"Word chosen is: {word}")

        return word


    def scoring(self,act_feed : list):

        if self.data.debug:
            print(act_feed)

        self.guess_count+=1

        for index,result in enumerate(act_feed):

            if GRAY in result:

                self.feedback[index][1] = 0

            if YELLOW in result:

                self.feedback[index][1] = 1

            if GREEN in result:

                self.feedback[index][1] = 2

        if self.data.debug:
            print(f"LETTER | SCORE | POSITION \n {self.feedback}")


        word = "".join(row[0] for row in self.feedback)

        score = sum(row[1] for row in self.feedback)


        if self.data.graphing:
            self.data.graphing_conversion(self.data.possible_words,word)

        if score == 10:

            self.win =True
            self.game_over = True
            self.end_game()
            return

        if self.guess_count >= 6:
            self.win = False
            self.game_over = True
            self.lose_game()
            return

        return


    def word_filter(self):
        # WANT TO ONLY ADD CHARACTERS HERE THAT WILL MATTER SO THEN THEY CAN BE SENT TO GET REMAINING
        gray_char = []
        yellow_char = []
        green_char = []

        for row in self.feedback:

            if row[1] == 2:

                green_char.append((row[0],row[2]))

            if row[1] == 1:
                #CHAR | POS
                yellow_char.append((row[0],row[2]))

            if row[1] == 0:
                gray_char.append(row[0])


        if gray_char:
            self.data.update_possible_words(gray_char)

        for pair in yellow_char:
            self.data.yellow_filter(pair)

        if green_char:
            self.data.update_specific_words(green_char)

        return


    def weight(self,candidate : str) -> float:

            known_green = sum(1 for row in self.feedback if row[1] == 2)
            correct_pos = sum(1 for row in self.feedback  if (row[1] == 2) and (candidate[row[2]] == row[0]) )

            return (correct_pos + 1) / (known_green + 1)


    def IG_scoring(self):

        H_X = self.entropy(self.data.word_count)

        if self.data.debug:
            print(f"H(X) : {H_X}")

        for candidate in self.data.possible_words:

            buckets = {}

            for possible_answer in self.data.possible_words:

                score = self.score_sort(candidate, possible_answer)

                if score not in buckets:
                    buckets[score] = 0

                buckets[score] +=1

            #use at your own risk, takes over a minute :)
            if self.data.super_debug:
                for key,value in buckets.items():
                    print(f"Bucket: {key} | Values: {value}")

            E_IG = H_X - self.entropy(buckets)
            W_G = self.weight(candidate)
            IG = E_IG * W_G

            if self.data.debug:
                print(f"Word: {candidate} | Entropy w/o weight {E_IG} | Entropy w/ weight {IG}")

            self.data.possible_words[candidate] = IG


        return


    def entropy(self,total) -> float:

        if isinstance(total, dict):
            bucket_size = sum(tot for tot in total.values())
            return sum((bucket_v / bucket_size) * (math.log2(bucket_v)) for bucket_v in total.values())

        return math.log2(total)


    def score_sort(self,candidate : str ,possible_answer : str) -> str:
        score = ""

        for index, char in enumerate(candidate):

            if char == possible_answer[index]:
                score += "2"

            elif char in possible_answer:
                score += "1"

            else:
                score += "0"

        return score


    def best_move(self) -> str:

        if self.data.super_debug:
            for key,value in self.data.possible_words.items():
                print(f"Word: {key}| Score: {value}")

        return max(self.data.possible_words,key= self.data.possible_words.get)


    def end_game(self):

        word = "".join(row[0] for row in self.feedback)
        print(f"WORDLE SOLVED! word was {word}")

        if self.data.graphing:
            self.data.display_graph()

        return


    def lose_game(self):
        word = "".join(row[0] for row in self.feedback)
        print(f"WORDLE WAS NOT SOLVED, CLOSEST GUESS {word}")
        return



