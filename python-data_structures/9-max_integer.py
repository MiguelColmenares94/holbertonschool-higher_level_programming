#!/usr/bin/python3


def max_integer(my_list=[]):
    """finds the biggest integer of a list.
    """

    if len(my_list) == 0:
        return (None)

    big_int = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > big_int:
            big_int = my_list[i]

    return (big_int)
