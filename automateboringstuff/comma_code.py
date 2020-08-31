def comma_code(words):
    sentence = ''
    for word in words:
        sentence += word
        if word == words[len(words) - 2]:
            sentence += ' and '
        elif word != words[len(words) - 1]:
            sentence += ', '

    return sentence
