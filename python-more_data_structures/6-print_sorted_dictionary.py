#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys
    """

    dic_to_list = list(a_dictionary.keys())
    dic_to_list.sort()

    for i in dic_to_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
