#!/usr/bin/python3


def print_last_digit(number):

    check = abs(number)
    check %= 10

    if check >= 0 and check <= 9:
        return(check)
    else:
        pass
