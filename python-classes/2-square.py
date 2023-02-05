#!/usr/bin/python3
"""class Square"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """Initializacion of objects, size must be an integer
            and greater or equal to 0

        Args:
            size(int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
