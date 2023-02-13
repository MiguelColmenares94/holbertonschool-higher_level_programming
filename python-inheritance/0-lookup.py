#!/usr/bin/python3
"""
Module that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """  returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
