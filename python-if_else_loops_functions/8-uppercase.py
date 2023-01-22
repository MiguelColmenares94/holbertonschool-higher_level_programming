#!/usr/bin/python3


def uppercase(str):

    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            j = ord(str[i]) - 32
        else:
            j = i
            print("{:c}".format(j), end="")
    print()
