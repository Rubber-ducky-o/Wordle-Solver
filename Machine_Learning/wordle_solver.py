from data_splitting import Data
import numpy as np
import matplotlib.pyplot as plt
import math
import random


class Solver:
    def __init__(self):
        probabilites = np.array([])
        self.data = Data()
        self.feedback = [['',0,''],
                         ['',0,''],
                         ['',0,''],
                         ['',0,''],
                         ['',0,'']]

    def insertion():

        #communication for js and python
        return

    def determinized_start(self):

        word =Data.randomized_start()

        for index, char in enumerate(word):
            self.feedback[index][0].append(char)

        #FUNCTION TO INSERT LETTERS INTO THE WORDLE GAME
        self.insertion()
        #THEN GET RESULTS BACK

        return



    def scoring(self,act_feed):
        #0 grey
        #1 yellow
        #2 green
        for index,result in enumerate(act_feed):
            match result:
                case "GREY":
                    self.feedback[index][0].append(0)
                case "YELLOW":
                    self.feedback[index][0].append(1)
                case "GREEN":
                    self.feedback[index][0].append(2)
                case _:
                    print("ERROR HAS OCCURED")



    def filter_pos(self):
        # WANT TO ONLY ADD CHARACTERS HERE THAT WILL MATTER SO THEN THEY CAN BE SENT TO GET REMAINING
    return



    def entropy(self):

        total = len(self.data.possible_words)



