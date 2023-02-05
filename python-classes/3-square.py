#!/usr/bin/python3
"""A class Square that defines a square by it's size"""


    class Square:
        """Defines a square class with some conditions"""
        def __init__(self, size=0):
            """Method to initialize objects
            
            Args:
                size (int): size of the square
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        def area(self):
            """Return: the current square area."""
            return (area=self.__size ** 2)
