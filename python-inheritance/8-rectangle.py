#!/usr/bin/python3
""" module containing a class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class used to represent a Rectangle inherited from BaseGeometry

    parameters
    ==========
    width : int
        width of Rectangle
    height : int
        height of Rectangle
    """
    def __init__(self, width, height):
        """ initializes the Rectangle """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
