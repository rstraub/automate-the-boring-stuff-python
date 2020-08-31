import unittest

from automateboringstuff.comma_code import comma_code


class CommaCode(unittest.TestCase):
    def test_comma_code_joins_two_values_with_and(self):
        result = comma_code(['one', 'two'])
        self.assertEqual('one and two', result)

    def test_comma_code_joins_three_values_with_comma_and_and(self):
        result = comma_code(['one', 'two', 'three'])
        self.assertEqual('one, two and three', result)

    def test_comma_code_returns_empty_string_when_empty_list_is_passed(self):
        result = comma_code([])
        self.assertEqual('', result)


if __name__ == '__main__':
    unittest.main()
