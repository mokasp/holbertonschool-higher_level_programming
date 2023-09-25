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

    methods
    =======
    area : int
        finds area of Rectangle
    """
    def __init__(self, width, height):
        """ initializes the Rectangle """
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height

    def __str__(self):
        """ returns string representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ returns area of the Rectangle """
        return self.__width * self.__height
