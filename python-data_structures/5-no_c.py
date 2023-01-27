#!/usr/bin/python3


def no_c(my_string):
    """removes all characters c and C from a string.
    """

    def no_c(my_string):

        if my_string is None:
            return []
        else:
            for i in range(len(my_string)):
                my_string.remove(c)
                my_string.remove(C)

        return (my_string)
