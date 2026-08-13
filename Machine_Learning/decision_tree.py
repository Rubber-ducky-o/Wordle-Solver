from data_splitting import Data
import numpy as np
import matplotlib.pyplot as plt
import math
import random


class Solver:
    def __init__(self):
        probabilites = np.array([])
        self.data = Data()



    def determinized_start(self):


        feedback = None


        return feedback

    def filter_pos(self):
        if self.data.all_words:
            for word in self.data.all_words:
                #if word does not fit the feedback then continue
                #else add it into the possible_words
                return

        for word in self.data.possible_words:
            #check if the new feedback fits the current word
            # list if not cut it down

            return


        self.data.possible_words.append()

    def entropy(self):

        total = len(self.data.possible_words)



