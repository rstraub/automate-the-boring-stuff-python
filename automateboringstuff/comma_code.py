def comma_code(words):
    sentence = ''
    for word in words:
        sentence += word
        sentence += get_join_symbol(word, words)

    return sentence


def get_join_symbol(word, words):
    if is_second_to_last(word, words):
        return ' and '
    elif is_last_word(word, words):
        return ''
    else:
        return ', '


def is_last_word(word, words):
    return word == words[-1]


def is_second_to_last(word, words):
    return len(words) >= 2 and word == words[-2]
