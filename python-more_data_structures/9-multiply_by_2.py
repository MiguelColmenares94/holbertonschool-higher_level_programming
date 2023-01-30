#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2
    """

    new_dic = a_dictionary.copy()
    key_list = list(new_dic)

    for i in key_list:
        new_dic[i] *= 2

    return(new_dic)
