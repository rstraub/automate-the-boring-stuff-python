import random


def guess_the_number():
    secret = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')

    for guesses in range(1, 7):
        print('Take a guess.')
        guess = int(input())
        print(guess)

        if guess < secret:
            print('Your guess is too low.')
        elif guess > secret:
            print('Your guess is too high.')
        else:
            print('Good job! You guessed my number in 4 guesses!')
            break

        guesses_left = 7 - guesses
        print(str(guesses_left) + ' guesses left.')


guess_the_number()
