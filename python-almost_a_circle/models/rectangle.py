#!/usr/bin/python3
"""This module contains the class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, this class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle's constructor

        Args:
            -width(int)
            -height(int)
            -x(int)
            -y(int)
            -id(int)
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, new_value):
        """
        Setter for private attribute width
        Args:
            -new_value(int)
        """
        if (type(new_value) is not int):
            raise TypeError("width must be an integer")
        elif (new_value <= 0):
            raise ValueError("width must be > 0")
        self.__width = new_value

    @property
    def height(self):
        """Getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, new_value):
        """
        Setter for private attribute height
        Args:
            -new_value(int)
        """
        if (type(new_value) is not int):
            raise TypeError("height must be an integer")
        elif (new_value <= 0):
            raise ValueError("height must be > 0")
        self.__height = new_value

    @property
    def x(self):
        """Getter for private attribute x"""
        return self.__x

    @x.setter
    def x(self, new_value):
        """
        Setter for private attribute x
        Args:
            -new_value(int)
        """
        if (new_value < 0):
            raise ValueError("x must be >= 0")
        self.__x = new_value

    @property
    def y(self):
        """Getter for private attribute y"""
        return self.__y

    @y.setter
    def y(self, new_value):
        """
        Setter for private attribute y
        """
        if (new_value < 0):
            raise ValueError("y must be >=0")
        self.__y = new_value
