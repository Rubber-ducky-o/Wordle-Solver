from Machine_Learning.data_splitting import Data
from Machine_Learning.wordle_solver import Solver
import unittest
import random


class TestData(unittest.TestCase):
    def test_base_object(self):

        data = Data()
        self.assertEqual(data.all_words,[])
        self.assertEqual(data.possible_words,dict())
        self.assertEqual(data.word_count,0)


    def test_word_count(self):
        data = Data()
        data.update_word_counter()

        self.assertEqual(data.word_count, 0)
        for i in range(0,10):
            data.possible_words[i] = 0

        data.update_word_counter()

        self.assertEqual(data.word_count,10)


    def test_initialization(self):
        data_fill = Data()
        data_fill.initialize()
        self.assertEqual(data_fill.word_count,3103)
        self.assertEqual(data_fill.possible_words,dict())

        data_em = Data()
        self.assertEqual(data_em.word_count, 0)
        self.assertEqual(data_em.possible_words,dict())


    def test_randomized_start(self):
        random.seed(42)
        data = Data()
        data.initialize()
        value = data.randomized_start()
        self.assertEqual(value,"strip")


    def test_update_possible_words(self):
        data = Data()
        lst1 = ["a","v","f"]
        lst2 = ["favor","depth","sings","paver","signs","joke","odors"]
        answer = {"depth": 0, "sings": 0,"signs":0,"joke":0,"odors":0}
        for word in lst2:
            data.possible_words[word] = 0


        data.update_possible_words(lst1)
        self.assertDictEqual(data.possible_words, answer)


    def test_update_specific_words(self):
        data = Data()
        data.possible_words.clear()

        data.all_words =  ["favor","depth","sings","paver","signs","joke","odors"]
        spots = [("a",1),("v",2)]

        answer = {"favor": "","paver": ""}
        data.update_specific_words(spots)
        self.assertDictEqual(data.possible_words,answer)

        data.possible_words = {"favor": 0,"depth": 0 ,"sings" : 0,"paver" : 0,"signs" : 0 ,"joke" :0 ,"odors": 0}
        spot = [("a",1),("v",2)]
        answer = {"favor": 0,"paver": 0}
        data.update_specific_words(spot)
        self.assertDictEqual(data.possible_words,answer)

    def test_yellow_filter(self):
        data = Data()
        data.all_words =  ["favor","depth","sings","paver","signs","joke","odors"]
        pair = ("s",0)
        answer = {"odors": ""}
        data.yellow_filter(pair)
        self.assertDictEqual(data.possible_words,answer)

        data = Data()
        data.possible_words = {"favor": 0,"depth": 0 ,"sings" : 0,"paver" : 0,"signs" : 0 ,"joke" :0 ,"odors": 0}
        pair = ("a", 0)
        answer = {"favor":0,"paver":0}
        data.yellow_filter(pair)
        self.assertDictEqual(data.possible_words,answer)

    def test_graphing_conversion(self):
        data = Data()
        points = {"words": 0,"fudge": 0}
        best_word = "plays"
        data.graphing_conversion(points,best_word)
        self.assertEqual(data.best_points[0],"plays")
        self.assertListEqual(data.pairwise,[[("words",0),("fudge",0)]])




class TestMachineLearning(unittest.TestCase):

    def test_determinized_start(self):
        solver = Solver()
        solver.data.initialize()
        random.seed(42)
        solver.determinized_start()
        self.assertEqual(solver.feedback[0][0],'s')
        self.assertEqual(solver.feedback[1][0],'t')
        self.assertEqual(solver.feedback[2][0],'r')
        self.assertEqual(solver.feedback[3][0],'i')
        self.assertEqual(solver.feedback[4][0],'p')


    def test_word_choice(self):
        random.seed(42)
        solver = Solver()
        solver.data.all_words = ["strip"]

        word = solver.word_choice()
        self.assertEqual(word,"strip")


        solver.data.possible_words = {"bangs": 1.2,"tiles":0.3}

        word = solver.word_choice()

        self.assertEqual(word,"bangs")


    def test_scoring(self):
        solver = Solver()
        s_card = ["rgb(58, 58, 60)","rgb(58, 58, 60)","rgb(83, 141, 78)","rgb(181, 159, 59)","rgb(58, 58, 60)"]

        solver.data.initialize()
        random.seed(42)
        solver.scoring(s_card)

        self.assertEqual(solver.feedback[0][1],0)
        self.assertEqual(solver.feedback[1][1],0)
        self.assertEqual(solver.feedback[2][1],2)
        self.assertEqual(solver.feedback[3][1],1)
        self.assertEqual(solver.feedback[4][1],0)

        s_card = ["rgb(83, 141, 78)","rgb(83, 141, 78)","rgb(83, 141, 78)","rgb(83, 141, 78)","rgb(83, 141, 78)"]

        solver.scoring(s_card)
        self.assertTrue(solver.win)
        self.assertTrue(solver.game_over)

        s_card = ["rgb(58, 58, 60)","rgb(83, 141, 78)","rgb(83, 141, 78)","rgb(83, 141, 78)","rgb(83, 141, 78)"]

        solver.guess_count =6
        solver.scoring(s_card)
        self.assertFalse(solver.win)
        self.assertTrue(solver.game_over)


    def test_word_filter(self):
        solver = Solver()
        solver.data.initialize()
        random.seed(42)
        solver.determinized_start()
        for row in solver.feedback:
            row[1] = 0
        solver.word_filter()
        self.assertNotEqual(solver.data.word_count,3103)

        solver.feedback = [['a',1,0],
                         ['b',0,1],
                         ['c',2,2],
                         ['d',1,3],
                         ['e',2,4]]

        solver.word_filter()
        self.assertEqual(solver.data.word_count,0)


    def test_IG_scoring(self):
        solver = Solver()
        solver.data.initialize()
        solver.data.possible_words.clear()


        solver.data.possible_words["tired"] = 0
        solver.data.possible_words["lefty"] = 0
        solver.data.possible_words["handy"] = 0
        solver.data.possible_words["souls"] = 0
        solver.data.possible_words["might"] = 0
        solver.data.update_word_counter()

        solver.IG_scoring()

        IG = solver.data.possible_words


        self.assertEqual(round(IG["tired"],3),2.322)
        self.assertEqual(round(IG["lefty"],3),2.322)
        self.assertEqual(round(IG["handy"],3),2.322)
        self.assertEqual(round(IG["souls"],3),1.371)
        self.assertEqual(round(IG["might"],3),2.322)













if __name__ == "__main__":
    unittest.main(buffer=False)