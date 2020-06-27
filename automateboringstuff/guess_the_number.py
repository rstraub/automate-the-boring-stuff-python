import random

print('Enter the difficulty you would like to play ("easy", "medium" or "hard"):')
difficulty = input()

def guess_the_number(amount_of_guesses):
    secret = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')

    for guessesTaken in range(1, amount_of_guesses + 1):
        print('Take a guess.')
        guess = int(input())
        print(guess)

        if guess < secret:
            print('Your guess is too low.')
        elif guess > secret:
            print('Your guess is too high.')
        else:
            print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
            break

        remaining_guesses = amount_of_guesses - guessesTaken
        print(str(remaining_guesses) + ' guesses left.')


if difficulty == 'medium':
    guess_the_number(6)
elif difficulty == 'hard':
    guess_the_number(3)
else:
    guess_the_number(10)
