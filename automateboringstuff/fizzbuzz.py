def fizz_buzz(number):
    result = str(number)
    if number % 15 == 0:
        result = 'FizzBuzz'
    elif number % 5 == 0:
        result = 'Buzz'
    elif number % 3 == 0:
        result = 'Fizz'
    return result


print(fizz_buzz(1))
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
