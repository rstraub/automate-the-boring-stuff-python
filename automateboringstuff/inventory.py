def display_inventory(inventory):
    print("Inventory:")
    print(formatted_items(inventory))
    print(total_items(inventory))


def formatted_items(inventory):
    display_message = ''
    for index, item in enumerate(inventory.items()):
        display_message += f'{formatted_item(item)}'
        is_last_item = index == (len(inventory.items()) - 1)
        if not is_last_item:
            display_message += '\n'
    return display_message


def formatted_item(item):
    item_amount = item[1]
    item_name = item[0]
    return f'{item_amount} {item_name}'


def total_items(inventory):
    total_amount = 0
    for item in inventory:
        total_amount += inventory.get(item)
    return f'Total number of items: {total_amount}'


def pickup_loot(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory


initial_inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

display_inventory(initial_inventory)

pickup_loot(initial_inventory, ['armour'])

print('--------------')
print('picked up loot')
print('--------------')

display_inventory(initial_inventory)
