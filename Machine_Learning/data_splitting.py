import random

class Data:

    def __init__(self):
        self.all_words = []
        self.possible_words = []
        self.word_count = 0
        self.start = None

    def initialize(self):
        with open("/local_wordle/5-letter-words.txt",encoding = "utf-8") as word_list:
            for word in word_list:
                self.all_words.append(word)
                self.word_count+=1
        return

    def randomized_start(self):
        self.start = random.choice(self.all_words)
        return

    def update_possible_words(self):

