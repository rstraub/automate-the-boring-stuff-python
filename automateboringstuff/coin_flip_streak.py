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


def streak_amount(coin_tosses):
    amount_of_streaks = 0
    current_streak = 0
    for index, coin_toss in enumerate(coin_tosses):
        if index == 0:
            continue
        previous = coin_tosses[index - 1]
        if coin_toss == previous:
            current_streak += 1
        else:
            current_streak = 0

        if current_streak == 6:
            amount_of_streaks += 1
            current_streak = 0

    return amount_of_streaks
