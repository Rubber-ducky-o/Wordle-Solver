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
        answer = {"favor": "", "paver": ""}
        for word in lst2:
            data.possible_words[word] = 0


        data.update_possible_words(lst1)
        self.assertDictEqual(data.possible_words, answer)

        data.possible_words.clear()

        for word in lst2:
            data.all_words.append(word)

        data.update_possible_words(lst1)

        self.assertDictEqual(data.possible_words,answer)


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


    def test_scoring(self):
        solver = Solver()
        s_card = ["GREY","GREY","GREEN","YELLOW","GREY"]

        solver.data.initialize()
        random.seed(42)
        solver.scoring(s_card)

        self.assertEqual(solver.feedback[0][1],0)
        self.assertEqual(solver.feedback[1][1],0)
        self.assertEqual(solver.feedback[2][1],2)
        self.assertEqual(solver.feedback[3][1],1)
        self.assertEqual(solver.feedback[4][1],0)


    def test_first_word_filter(self):
        solver = Solver()
        solver.data.initialize()
        random.seed(42)
        solver.determinized_start()
        solver.first_word_filter()
        self.assertNotEqual(solver.data.word_count,3103)

    def test_bucket_scoring(self):
        solver = Solver()
        solver.data.initialize()
        random.seed(42)
        solver.determinized_start()
        s_card = ["GREY","YELLOW","GREEN","GREEN","GREY"]
        solver.scoring(s_card)

        solver.data.possible_words.clear()
        solver.data.possible_words["tired"] = ""
        solver.data.possible_words["lefty"] = ""
        solver.bucket_scoring()
        self.assertEqual(solver.data.scores["00010"],1)

        self.assertEqual(solver.data.scores["11200"],1)













if __name__ == "__main__":
    unittest.main(buffer=False)