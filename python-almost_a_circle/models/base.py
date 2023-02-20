#!/usr/bin/python3
"""
This module contains the class Base
"""
import json


class Base:
    """
    This class is the “base” of all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation
        of list_dictionaries
        - list_dictionary: must be a list of dictionary
        - Return: string of dictionary in json format"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string
        representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for objs in list_objs:
                dictionary = objs.to_dictionary()
                result.append(dictionary)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON
        string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
