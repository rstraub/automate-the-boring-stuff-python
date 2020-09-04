def display_inventory(inventory):
    total_items(inventory)


def formatted_item(item):
    item_amount = item[1]
    item_name = item[0]
    return f'{item_amount} {item_name}'


def total_items(inventory):
    total_amount = 0
    for item in inventory:
        total_amount += inventory.get(item)
    return f'Total number of items: {total_amount}'
