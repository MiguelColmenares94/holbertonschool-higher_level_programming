#!/usr/bin/python3
"""Method that define Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override __str__ method from Rectangle"""
        string = "[Square] ({:}) {:}/{:} - {:}"
        string = string.format(self.id, self.x, self.y, self.width)
        return string

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, new_value):
        """Setter for size"""
        self.width = new_value
        self.height = new_value

    def update(self, *args, **kwargs):
        """refresh the values of square attributes"""
        args_list = ["id", "width", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        key_list = ["id", "size", "x", "y"]
        value_list = [self.id, self.width, self.x, self.y]
        return dict(zip(key_list, value_list))
