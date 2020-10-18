def format_data(data):
    formatted_data = justify_column_texts(data)

    # Build the result string
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

    return "\n".join(row_texts)


def justify_column_texts(data):
    formatted_data = []
    for column in data:
        longest_string = 0
        for row in column:
            length = len(row)
            if length > longest_string:
                longest_string = length

        formatted_column = []
        for row in column:
            formatted_item = str(row).rjust(longest_string)
            formatted_column.append(formatted_item)
        formatted_data.append(formatted_column)
    return formatted_data


def print_table(data):
    print(format_data(data))
