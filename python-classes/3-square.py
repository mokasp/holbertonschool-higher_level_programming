#!/usr/bin/python3
""" a module containing a class Square """


class Square:
    """ a class representing an empty Square

        attributes
        ----------
        size : int, optional
            size of Square

        methods
        ----------
        area():
            returns current area of Square
    """

    def __init__(self, size=0):
        """ constructs all attributes for a Square

        parameters
        ----------
        size : int, optional
            size of Square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return area of Square """

        return self.__size * self.__size
