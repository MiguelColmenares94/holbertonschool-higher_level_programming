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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if (type(new_value) is not int):
            raise TypeError("x must be an integer")
        elif (new_value < 0):
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
        if (type(new_value) is not int):
            raise TypeError("y must be an integer")
        elif (new_value < 0):
            raise ValueError("y must be >= 0")
        self.__y = new_value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Print Rectangle with "#" character"""
        for y in range(0, self.y):
            print()
        for j in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for i in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Human readable string for understanding Rectangle instance"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        string = string.format(self.id, self.x, self.y, self.width,
                               self.height)
        return string

    def update(self, *args, **kwargs):
        """Assing an argument to each attribute"""
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))
