#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """replaces an element from a list like in C
    """

    if idx < 0:
        return (my_list)
    elif idx > (len(my_list) - 1):
        return (my_list)
    else:
        del my_list[idx]
        return (my_list.insert(idx, element))
