#!/usr/bin/python3


def no_c(my_string):
    """removes all characters c and C from a string.
    """

    def no_c(my_string):

        for i in range(len(my_string)):
            if my_string[i] == 'c' or my_string[i] == 'C':
                del my_string[i]

    return (my_string)
