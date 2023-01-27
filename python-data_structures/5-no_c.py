#!/usr/bin/python3


def no_c(my_string):
    """removes all characters c and C from a string.
    """

    copy = my_string.copy()
    for i in range(len(copy)):
        if copy[i] == chr(99) or copy[i] == chr(67):
            copy.remove(i)

    return (copy)
