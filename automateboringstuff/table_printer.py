def format_table(data):
    justified_table = justify_table(data)
    row_texts = get_row_texts(justified_table)

    return "\n".join(row_texts)


def justify_table(data):
    formatted_data = []
    for column in data:
        formatted_column = justify_column(column)
        formatted_data.append(formatted_column)
    return formatted_data


def justify_column(column):
    longest_string = get_longest_string_length(column)
    justified_column = []
    for row in column:
        justified_row = str(row).rjust(longest_string)
        justified_column.append(justified_row)
    return justified_column


def get_longest_string_length(column):
    longest_string = 0
    for row in column:
        length = len(row)
        if length > longest_string:
            longest_string = length
    return longest_string


def get_row_texts(formatted_data):
    amount_of_columns = len(formatted_data)
    amount_of_rows = len(formatted_data[0])
    row = 0
    row_texts = []
    while row < amount_of_rows:
        row_text = ""
        column = 0
        while column < amount_of_columns:
            row_text += formatted_data[column][row]

            if column + 1 is not amount_of_columns:
                row_text += " "

            column += 1
        row_texts.append(row_text)

        row += 1
    return row_texts


def print_table(data):
    print(format_table(data))
