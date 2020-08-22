def collatz(number):
    if is_even(number):
        return number // 2
    else:
        return 3 * number + 1


def is_even(number):
    return number % 2 == 0


def run():
    number = 0
    try:
        number = int(input())
    except ValueError:
        print('You must enter a number')

    result = number
    while result != 1:
        result = collatz(result)
        print(result)


run()
