import random


def random_num(amount):
    for num in range(amount):
        print(random.randint(1, 10))


random_num(10)
