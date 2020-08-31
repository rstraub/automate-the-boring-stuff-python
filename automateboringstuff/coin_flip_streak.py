def as_heads_or_tails(number):
    if number == 1:
        return 'H'
    else:
        return 'T'


def coin_tosses(amount):
    return [as_heads_or_tails(1)]
