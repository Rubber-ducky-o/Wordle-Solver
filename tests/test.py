from Machine_Learning import wordle_solver, data_splitting
import unittest


class TestData(unittest.TestCase):
    def test_base_object(self):
        data = wordle_solver.Data()
        self.assertEqual(data.all_words,[])
        self.assertEqual(data.possible_words,None)
        self.assertEqual(data.word_count,0)


    def test_word_count(self):
        data = wordle_solver.Data()
        data.word_counter()


    def test_initialization(self):
        data = wordle_solver.Data()
        data.initialize()

        self.assertEqual()


    def test_randomized_start(self):
        return


    def test_update_possible_words(self):
        return

class TestSolver(unittest.TestCase):
    def test_initialization(self):


        return


if __name__ == "__main__":
    unittest.main()