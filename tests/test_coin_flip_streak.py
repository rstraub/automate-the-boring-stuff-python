import unittest

from automateboringstuff.coin_flip_streak import as_heads_or_tails, coin_tosses, is_streak


class CoinFlipStreak(unittest.TestCase):
    def test_should_return_heads_given_one(self):
        result = as_heads_or_tails(1)
        self.assertEqual('H', result)

    def test_should_return_tails_given_zero(self):
        result = as_heads_or_tails(0)
        self.assertEqual('T', result)

    def test_should_return_one_coin_toss_given_one(self):
        result = coin_tosses(1)
        self.assertEqual(1, len(result))
        self.assertTrue('H' in result or 'T' in result)

    def test_should_return_x_coin_tosses_given_x(self):
        result = coin_tosses(100)
        self.assertEqual(100, len(result))
        self.assertTrue('T' in result)
        self.assertTrue('H' in result)

    def test_should_return_false_given_streak_of_five_or_less(self):
        result = is_streak(('H', 'H', 'H', 'H', 'H'))
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
