#!/usr/bin/python3


def uppercase(str):

    for i in str:
        if i != NULL:
            print("{:c}".format((ord(str[i] - 32))), end="")
        else:
            print("\n")
