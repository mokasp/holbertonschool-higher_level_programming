#!/usr/bin/python3
""" module containing a class BaseGeometry """


class BaseGeometry():
    """ a class used to represent BaseGeometry

    methods
    ---------------
    area : returns area of instance
    """
    def __init__(self):
        """ initialize """

    def area(self):
        """ returns area of an instance """
        raise Exception("area() is not implemented")
