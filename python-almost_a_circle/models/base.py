#!/usr/bin/python3
""" module containing a class Base to create shapes """
import json


class Base:
    """ a class representing a Base object to create shapes from """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructs all attributes of the Rectangle

        .....

        parameters
        ----------
        id : int, optional
            id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of a dict repr"""
        if list_dictionaries is None and len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
