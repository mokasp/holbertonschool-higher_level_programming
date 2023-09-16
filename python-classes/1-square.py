#!/usr/bin/python3
""" a module containing a class Square """


class Square:
    """ a class representing an empty Square

        attributes
        ----------
        size : int
            size of Square
    """

    def __init__(self, size):
        """ constructs all attributes for a Square

        parameters
        ----------
        size : int
            size of Square
        """
        self.__size = size
