import unittest

from automateboringstuff.table_printer import format_data


class MyTestCase(unittest.TestCase):
    def test_should_format_data_given_single_column(self):
        table_data = [["apple", "orange", "banana"]]
        expected = """ apple
orange
banana"""

        result = format_data(table_data)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
