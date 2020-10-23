import unittest
from code_challenges.wolf_in_sheeps_clothing import warn_the_sheep


class MyTestWolfCase(unittest.TestCase):

    def test_method_exists(self):
        self.assertTrue(warn_the_sheep())

    def test_returns_pls_go_away_sentence(self):
        sentence_to_test = 'Pls go away and stop eating my sheep'
        self.assertEqual(sentence_to_test, warn_the_sheep())

    def test_returns_warning_sentence(self):
        sentence_to_test = 'Oi! Sheep number N! You are about to be eaten by a wolf!'
        self.assertEqual(sentence_to_test, warn_the_sheep('something'))


if __name__ == '__main__':
    unittest.main()
