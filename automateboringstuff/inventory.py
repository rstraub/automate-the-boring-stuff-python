def display_inventory(inventory):
    total_items(inventory)


def total_items(inventory):
    total_amount = 0
    for item in inventory:
        total_amount += inventory.get(item)
    return f'Total number of items: {total_amount}'
