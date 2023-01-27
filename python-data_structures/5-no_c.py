#!/usr/bin/python3


def no_c(my_string):
    """ removes all characters c and C from a string
    """

    my_list = list(my_string)
    for i in my_list[0:]:
        if i == 'c' or i == 'C':
            my_list.remove(i)

    return ("".join(my_list))
