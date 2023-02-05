#!/usr/bin/python3
"""class Square"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """
        Args:
            size(int): size of the square.

        Attributes:
            Private instance attribute: size
               - size must be an int
               - size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method: that returns the current square area

        Returns:
            The area of the square
        """
        return (area=self.__size ** 2)
