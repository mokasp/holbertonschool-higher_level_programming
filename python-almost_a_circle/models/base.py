#!/usr/bin/python3
""" module containing a class Base to create shapes """
import json
import os


class Base:
    """ a class representing a Base object to create shapes from

    Class Attributes
    ================
    nb_objects - int
        number of instances of Base

    Instance Attributes
    ===================
    id - int
        identity of object

    Static Methods
    --------------
    to_json_string : JSON string
        returns the JSON string representation of a dict repr
    from_json_string :
        converts JSON string to python object

    Class Methods
    -------------
    save_to_file :
        writes list of instances of Base to a file as its JSON represention
    create :
        returns an instance with all attributes already set
    load_from_file :
        returns a list of instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructs all attributes of the Rectangle

        .....

        parameters
        ==========
        id - int, optional
            id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of a dict repr

            parameters
            ==========
            list_dictionaries - list
                list of dictionaries of attributes for object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function that writes a list of instances of Base to a text file \
            as its JSON represention

            parameters
            ==========
            list_obj - list
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

    @staticmethod
    def from_json_string(json_string):
        """ function that converts JSON string to python object

            parameters
            ==========
            json_string - JSON string
                json string to convert to python object
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set

            parameters
            ==========
            dictionary - dict
                dictionary containing attributes for new object
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ class method that returns a list of instances """
        filename = f"{cls.__name__}.json"
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename):
            with open(filename, "r") as read_file:
                instances = read_file.read()
            temp = cls.from_json_string(instances)
            new_instances = []
            for item in temp:
                new_instances.append(cls.create(**item))
            return new_instances
        else:
            return []
