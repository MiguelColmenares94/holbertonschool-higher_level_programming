#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers.
    """

    for row in matrix:
        for val in row:
            print("{:d}".format(val), end="")
            if val != (len(matrix) - 1):
                print(" ", end="")

        print()
