#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """  adds 2 tuples
    """

    tupA = len(tuple_a)
    tupB = len(tuple_b)

    if tupA == 0:
        tupA1 = 0
        tupA2 = 0
    elif tupA == 1:
        tupA1 = tuple_a[0]
        tupA2 = 0
    else:
        tupA1 = tuple_a[0]
        tupA2 = tuple_a[1]

    if tupB == 0:
        tupB1 = 0
        tupB2 = 0
    elif tupB == 1:
        tupB1 = tuple_b[0]
        tupB2 = 0
    else:
        tupB1 = tuple_b[0]
        tupB2 = tuple_b[1]

    newTup = (a1 + b1, a2 + b2)

    return (newTup)
