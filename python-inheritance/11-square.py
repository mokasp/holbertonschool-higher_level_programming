#!/usr/bin/python3
""" module containing a class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class used to represent a Square inherited from Rectangle

    parameters
    ==========
    size : int
        size of one side of Square

    methods
    =======
    area : int
        finds area of Square
    """
    def __init__(self, size):
        """ initializes the Square """
        super(Square, self).__init__(size, size)
        self.__size = size

    def __str__(self):
        """ str representation of Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
