#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list
    (only once for each integer)
    """

    non_rep = set(my_list)
    n = 0

    for i in non_rep:
        n += i

    return (n)
