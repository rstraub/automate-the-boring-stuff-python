from random import randint


def random_num(amount):
    for num in range(amount):
        print(randint(1, 10))


random_num(10)
