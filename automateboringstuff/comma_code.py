def comma_code(words):
    sentence = ''
    for word in words:
        sentence += word
        sentence += get_join_symbol(word, words)

    return sentence


def get_join_symbol(word, words):
    if word == words[len(words) - 2]:
        return ' and '
    elif word != words[len(words) - 1]:
        return ', '
    else:
        return ''
