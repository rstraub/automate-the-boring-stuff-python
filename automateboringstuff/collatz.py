def collatz(number):
    if is_even(number):
        return number // 2
    else:
        return 3 * number + 1


def is_even(number):
    return number % 2 == 0


def run():
    try:
        number = int(input())
        result = number
        while result != 1:
            result = collatz(result)
            print(result)
    except ValueError:
        print('You must enter a number')


run()
