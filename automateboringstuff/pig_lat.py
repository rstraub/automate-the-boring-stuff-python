# English to pig latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = []
for word in message.split():
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]

    if len(word) == 0:
        pig_latin.append(prefix_non_letters)

    suffix_non_letters = ''

    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    prefix_consonants
