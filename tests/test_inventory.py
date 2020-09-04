import unittest

from automateboringstuff.inventory import total_items, formatted_item, formatted_items


class Inventory(unittest.TestCase):
    def test_should_give_total_items_of_zero_given_an_empty_inventory(self):
        inventory = {}
        result = total_items(inventory)
        self.assertEqual('Total number of items: 0', result)

    def test_should_give_total_items_of_one_given_an_inventory_with_a_single_item(self):
        inventory = {
            'arrow': 1
        }
        result = total_items(inventory)
        self.assertEqual('Total number of items: 1', result)

    def test_should_give_total_items_of_two_given_inventory_with_multiple_items(self):
        inventory = {
            'arrow': 1,
            'potions': 1
        }
        result = total_items(inventory)
        self.assertEqual('Total number of items: 2', result)

    def test_should_display_inventory_item_given_inventory_with_at_least_one_item(self):
        item = ['arrow', 1]
        result = formatted_item(item)
        self.assertEqual('1 arrow', result)

    def test_should_format_inventory_items_given_inventory_with_multiple_items(self):
        inventory = {
            'arrow': 1,
            'potion': 1
        }

        result = formatted_items(inventory)

        self.assertEqual('1 arrow\n1 potion', result)

if __name__ == '__main__':
    unittest.main()
