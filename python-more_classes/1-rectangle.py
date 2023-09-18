#!/usr/bin/python3
"""
a module containing a Rectangle
"""


class Rectangle:
    """
    a class used to represent a Rectangle

    .....

    attributes
    ----------
    width : int, optional
        width of the Rectangle
    height : int, optional
        heigth of the Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        constructs all attributes of the Rectangle

        .....

        parameters
        ----------
        width : int, optional
            width of the Rectangle
        height : int, optional
            heigth of the Rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ method to get the current width of the Rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ method to set new width of the Rectangle """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width musth be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """ method to get the current height of the Rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ method to set new height of the Rectangle """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height musth be >=0")
        else:
            self.__height = value
