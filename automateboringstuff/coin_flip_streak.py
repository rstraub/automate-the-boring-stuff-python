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


def streak_amount(tosses):
    amount_of_streaks = 0
    current_streak = 0
    for index, coin_toss in enumerate(tosses):
        if index == 0:
            current_streak = 1
            continue

        previous = tosses[index - 1]
        if coin_toss == previous:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak == 6:
            amount_of_streaks += 1
            current_streak = 0

    return amount_of_streaks


def coin_flip_streak():
    number_of_streaks = streak_amount(coin_tosses(10000))
    print('Amount of streaks:', number_of_streaks)
    print('Chance of streak: %s%%' % (number_of_streaks / 100))


coin_flip_streak()
