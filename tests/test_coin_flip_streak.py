import unittest

from automateboringstuff.coin_flip_streak import as_heads_or_tails, coin_tosses


class CoinFlipStreak(unittest.TestCase):
    def test_should_return_heads_given_one(self):
        result = as_heads_or_tails(1)
        self.assertEqual('H', result)

    def test_should_return_tails_given_zero(self):
        result = as_heads_or_tails(0)
        self.assertEqual('T', result)

    def test_should_return_coin_flip_list_given_one(self):
        result = coin_tosses(1)
        self.assertEqual(1, len(result))
        self.assertTrue(result[0] == ('H' or 'T'))


if __name__ == '__main__':
    unittest.main()
