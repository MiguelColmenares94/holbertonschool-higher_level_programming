#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific
       position without modifying the original list (like in C)
    """

    new_list = my_list.copy()

    if idx < 0:
        return (new_list)
    elif idx > (len(new_list) - 1):
        return (new_list)
    else:
        del new_list[idx]
        new_list.insert(idx, element)
        return (new_list)
