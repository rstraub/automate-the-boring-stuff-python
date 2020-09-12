#! python3

"""
List of animals
List of cars
List of things
"""

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for line in range(len(lines)):
    lines[line] = f'* {lines[line]}'
text = '\n'.join(lines)

pyperclip.copy(text)
