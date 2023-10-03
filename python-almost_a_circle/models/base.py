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
        if list_dictionaries is None and len(list_dictionaries) != 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function that writes a list of instances of Base to a text file \
            as its JSON represention

        parameters
        ==========
        list_obj : list
            list of instances of Base
    """
        filename = f"{cls.__name__}.json"
        new_list = []
        if list_objs is None:
            with open(filename, "w") as write_file:
                write_file.write("[]")
        else:
            for item in list_objs:
                my_obj = item.to_dictionary()
                new_list.append(my_obj)
            the_obj = cls.to_json_string(new_list)
            with open(filename, "w") as write_file:
                write_file.write(the_obj)

    def from_json_string(json_string):
        """ function that converts JSON string to object

        parameters
        ==========
        json_string : JSON string
            json string to convert to object
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set

            parameters
            ==========
            dictionary : dict
                dictionary containing attributes for new object
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy
