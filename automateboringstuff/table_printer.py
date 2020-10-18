def format_data(data):
    longest_string = len(data[0])
    formatted_data = []
    for column in data:
        for row in column:
            length = len(row)
            if length > longest_string:
                longest_string = length

        for row in column:
            formatted_item = str(row).rjust(longest_string)
            formatted_data.append(formatted_item)

    return "\n".join(formatted_data)
