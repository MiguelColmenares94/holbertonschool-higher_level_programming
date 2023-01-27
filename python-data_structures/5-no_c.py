#!/usr/bin/python3


def no_c(my_string):
    """removes all characters c and C from a string.
    """
        for i in range(len(my_string)):
            if my_string[i] == chr(99) or my_string[i] == chr(67):
                del my_string[i]

    return (my_string)
