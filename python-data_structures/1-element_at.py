#!/usr/bin/python3


def element_at(my_list, idx):
    """retrieves an element from a list like in C
    """

    if idx < 0:
        return None

    if idx > len(my_list):
        return None

    print("Element at index {} is {}".format(idx, my_list[idx]))
