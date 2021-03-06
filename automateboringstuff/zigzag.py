import sys
import time


def zigzag():
    indent = 0
    indentIncreasing = True
    maxIndent = 20
    minIndent = 0
    symbols = '*******'

    try:
        while True:
            print(' ' * indent, end='')
            print(symbols)
            time.sleep(0.1)
            if indentIncreasing:
                indent = indent + 1
                if indent == maxIndent:
                    indentIncreasing = False
            else:
                indent = indent - 1
                if indent == minIndent:
                    indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()


zigzag()
