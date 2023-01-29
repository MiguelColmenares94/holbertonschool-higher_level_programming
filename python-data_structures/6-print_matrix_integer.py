#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers.
    """

    for row in range(len(matrix)):
        for val in matrix[row]:
            print("{:d}".format(matrix[row][val]), end="")
            if val != (len(matrix) - 1):
                print(" ", end="")

        print()
