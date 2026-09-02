from Machine_Learning.data_splitting import Data
import numpy as np
import matplotlib.pyplot as plt
import math
import random


class Solver:
    def __init__(self):
        self.data = Data()
        # LETTER | VALUE | POSITION
        self.feedback = [['',0,0],
                         ['',0,1],
                         ['',0,2],
                         ['',0,3],
                         ['',0,4]]

        self.probabilites = []



    def is_empty(self):
        return bool(self.data.possible_words)


    def insertion(self,word):
        pass
        #communication for js and python


    def determinized_start(self):

        word = self.data.randomized_start()

        for index, char in enumerate(word):
            self.feedback[index][0] = char

        #FUNCTION TO INSERT LETTERS INTO THE WORDLE GAME
        self.insertion(word)
        #THEN GET RESULTS BACK

        return



    def scoring(self,act_feed):
        #0 grey
        #1 yellow
        #2 green
        for index,result in enumerate(act_feed):
            match result:
                case "GREY":
                    self.feedback[index][1] = 0
                case "YELLOW":
                    #THIS CASE POSITION WOULD NOT MATTER:
                    self.feedback[index][1] = 1
                case "GREEN":
                    self.feedback[index][1] = 2
                case _:
                    print("ERROR HAS OCCURED")

        return



    def first_word_filter(self):
        # WANT TO ONLY ADD CHARACTERS HERE THAT WILL MATTER SO THEN THEY CAN BE SENT TO GET REMAINING
        char_list = []

        for index in range(len(self.feedback)):
            if self.feedback[index][1] == 2 or self.feedback[index][1] == 1:
                char_list.append(self.feedback[index][0])

        self.data.update_possible_words(char_list)

    def bucket_scoring(self):
        #LETTER | VALUE | POSITION
        guessed_word = self.feedback[0][0] + self.feedback[1][0] + self.feedback[2][0] +self.feedback[3][0] +self.feedback[4][0]
        #1 CONVERT TO CHARACTERS THEN LOOP THROUGH EACH CHARACTER COMPARING
        #2 CHECK IF IN
        #PRIORITIZE SCORES 2, THEN 1 THEN 0 SO WE KNOW, IF

        #SCORE 2: same spot  = 2, not in same spot = 1
        #SCORE 1: same spot = 0, not in same spot = 1
        #SCORE 0: same spot = 0, different spot = 0
        for word in self.data.possible_words:
            #WORD = POSSIBLE WORDS
            #print(f"CURRENT WORD IS {word}")
            for index, char in enumerate(word):
                #ITERATING THROUGH THE WORD
                #print(f"CURRENT CHAR FROM WORD WITH INDEX IS {char} | {index}")
                if char in guessed_word:
                    #print(f"CHAR : {char} IS IN GUESSED WORD: {guessed_word}")
                    #CHECK REWARD BY FINDING INDEX OF CHARACTER
                    for index_g in range(4):


                        letter = self.feedback[index_g][0]
                        #print(f"LETTER : {letter} IS BEING COMPARED TO CHAR {char}")

                        if letter == char:
                            #print(f"LETTER : {letter} WAS MATCH FOR CHAR:  {char}")

                            score = self.feedback[index_g][1]
                            position = self.feedback[index_g][2]
                            #print(f"SCORE : {score} OF CHAR: {char}  WITH POSITION : {position}")

                            match score:
                                case 0:
                                    self.data.possible_words[word] += "0"
                                    #print(f"CASE 0 : 0 POINTS GIVEN")

                                    break

                                case 1:
                                    if position == index:
                                        self.data.possible_words[word]+="0"
                                        #print(f"CASE 1 : 0 POINTS GIVEN")
                                    if position != index:
                                        self.data.possible_words[word]+="1"
                                        #print(f"CASE 1 : 1 POINTS GIVEN")

                                    break

                                case 2:
                                    if position == index:
                                        self.data.possible_words[word]+="2"
                                        #print(f"CASE 2 : 2 POINTS GIVEN")

                                    if position != index:
                                        self.data.possible_words[word]+="1"
                                        #print(f"CASE 2 : 2 POINTS GIVEN")

                                    break

                        else:
                            #print(f"LETTERS DO NOT MATCH NOTHING GIVEN NEXT")

                            continue
                else:
                    self.data.possible_words[word] += "0"
                    #print(f"CHAR WAS NOT IN WORD GIVEN 0")

            self.data.scores[self.data.possible_words[word]] += 1






    def main_brain(self):
        pass










