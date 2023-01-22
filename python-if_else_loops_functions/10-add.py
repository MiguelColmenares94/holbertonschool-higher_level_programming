#!/usr/bin/python3


def add(a, b):

    checkA = isinstance(a, int)
    checkB = isinstance(b, int)

    if (checkA and checkB) == 1:
        return(a + b)
    else:
        pass
