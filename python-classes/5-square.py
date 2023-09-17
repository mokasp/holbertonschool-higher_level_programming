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
        self.__size = size

    @property
    def size(self):
        """ returns private attribute size of Square """

        return self.__size

    @size.setter
    def size(self, value):
        """ sets new value for private attribute size of Square

        parameters
        ----------
        value : int
            new size of Square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return area of Square """

        return self.__size * self.__size

    def my_print(self):
        """ prints the Square """

        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end="")
            print()
