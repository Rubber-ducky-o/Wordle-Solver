import random
from pathlib import Path
import itertools

class Data:

    def __init__(self):
        self.all_words = list()
        self.possible_words = dict()
        self.word_count = 0
        self.scores = dict()

    def update_word_counter(self):
        if self.possible_words:
            self.word_count =  len(self.possible_words)
            return
        self.word_count = len(self.all_words)
        return


    def initialize(self):


        dir_ = Path(__file__).resolve().parent.parent

        full_path = dir_ / "Local_wordle" / "5-letter-words.txt"

        with open(full_path, "r", encoding = "utf-8") as word_list:
            for word in word_list:
                self.all_words.append(word.strip())
        self.word_count = len(self.all_words)

        digits = '012'
        length = 5

        self.scores = {"".join(seq): 0 for seq in itertools.product(digits,repeat = length)}
        return


    def randomized_start(self):
        if self.possible_words:
            word = random.choice(self.possible_words)
            self.possible_words.pop(word)
            self.update_word_counter()

            return word

        word = random.choice(self.all_words)
        self.all_words.remove(word)
        self.update_word_counter()

        return word



    def update_possible_words(self,characters: list):

        if len(self.possible_words) == 0:
            self.possible_words = {k: "" for k in self.all_words if any(chars in k for chars in characters)}
            self.update_word_counter()
            return
        self.possible_words = {k: "" for k in self.possible_words if any(chars in k for chars in characters)}
        self.update_word_counter()
        self.all_words.clear()
        return






