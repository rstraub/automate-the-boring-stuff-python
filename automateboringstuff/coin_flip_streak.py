from random import randint


def as_heads_or_tails(number):
    if number == 1:
        return 'H'
    else:
        return 'T'


def coin_tosses(amount):
    result = []
    for toss in range(amount):
        result.append(as_heads_or_tails(randint(0, 1)))
    return result
