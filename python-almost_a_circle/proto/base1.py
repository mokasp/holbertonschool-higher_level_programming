#!/usr/bin/python3
""" module containing a class Base to create shapes """


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
