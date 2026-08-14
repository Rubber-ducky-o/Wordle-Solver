import random

class Data:

    def __init__(self):
        self.all_words = []
        self.possible_words = None
        self.word_count = 0

    def word_count(self):
        if self.possible_words:
            self.word_count =  len(self.word_possible_words)
            return
        self.word_count = len(self.all_words)
        return


    def initialize(self):
        with open("/local_wordle/5-letter-words.txt",encoding = "utf-8") as word_list:
            for word in word_list:
                self.all_words.append(word)

        self.word_count = len(self.all_words)
        return


    def randomized_start(self):
        return random.choice(self.all_words)


    def update_possible_words(self,characters: list):

        if self.possible_words:
            self.possible_words = [char for char in self.all_words if any(chars in char for chars in characters)]
            return
        self.possible_words = [ char for char in self.all_words if any(chars in char for chars in characters)]

        return







