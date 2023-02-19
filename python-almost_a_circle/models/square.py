#!/usr/bin/python3
"""Method that define Square class"""
from models.base import Base


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override __str__ method from Rectangle"""
        string = "[Square] ({:}) {:}/{:} - {:}"
        string = string.format(self.id, self.x, self.y, self.width)
        return string
