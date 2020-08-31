import unittest

from automateboringstuff.coin_flip_streak import as_heads_or_tails, coin_tosses, streak_amount


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

    def test_should_return_zero_given_streak_of_five_or_less(self):
        result = streak_amount(('H', 'H', 'H', 'H', 'H', 'T'))
        self.assertEqual(0, result)

    def test_should_return_one_given_streak_of_six(self):
        result = streak_amount(('H', 'H', 'H', 'H', 'H', 'H'))
        self.assertEqual(1, result)

    def test_should_return_two_given_two_broken_streaks_of_six(self):
        result = streak_amount(('H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'H', 'H', 'H', 'H', 'H'))
        self.assertEqual(2, result)

    def test_should_return_zero_for_broken_streak(self):
        result = streak_amount(('H', 'H', 'H', 'T', 'H', 'H', 'H'))
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
