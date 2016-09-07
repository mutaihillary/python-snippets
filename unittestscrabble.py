import unittest

from scrabble import scrabble_score


class WordTest(unittest.TestCase):
    def test_invalid_word_scrabble_scrabble_scores_zero(self):
        self.assertEqual(0, scrabble_score(''))
        self.assertEqual(0, scrabble_score(' \t\n'))
        self.assertEqual(0, scrabble_score('hous3'))
        self.assertEqual(0, scrabble_score('wo rd'))

    def test_scrabble_scores_very_short_word(self):
        self.assertEqual(1, scrabble_score('a'))

    def test_scrabble_scores_other_very_short_word(self):
        self.assertEqual(4, scrabble_score('f'))

    def test_simple_word_scrabble_scores_the_number_of_letters(self):
        self.assertEqual(6, scrabble_score("street"))

    def test_complicated_word_scrabble_scores_more(self):
        self.assertEqual(22, scrabble_score("quirky"))

    def test_scrabble_scores_are_case_insensitive(self):
        self.assertEqual(41, scrabble_score("OxyphenButazone"))

if __name__ == '__main__':
    unittest.main()