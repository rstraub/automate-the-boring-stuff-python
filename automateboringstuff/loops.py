def while_loop():
    i = 1
    while i <= 10:
        print(i)
        i += 1
        if i == 5:
            break


while_loop()


def for_loop():
    for i in range(11, 21):
        if i == 15:
            continue
        print(i)


for_loop()


def gauss():
    total = 0
