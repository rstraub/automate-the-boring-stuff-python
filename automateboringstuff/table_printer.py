def format_data(data):
    longest_string = len(data[0])
    for item in data:
        length = len(item)
        if length > longest_string:
            longest_string = length

    formatted_data = []
    for item in data:
        formatted_item = str(item).rjust(longest_string)
        formatted_data.append(formatted_item)

    return "\n".join(formatted_data)
