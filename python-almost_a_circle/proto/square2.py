#!/usr/bin/python3
""" module containing a class Square inherited from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class used to represent a Sqaure

    .....

    attributes
    ----------
    size : int, optional
        width of the Square
    x : int, optional
        x axis
    y : int, optional
        y axis
    id : int, optional
        identity of object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructs all attributes of the Rectangle

        .....

        parameters
        ----------
        size : int, optional
            size of the Square
        x : int, optional
            x axis
        y : int, optional
            y axis
        id : int, optional
            identity of Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ returns string representation of Square """
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ method to get the current size of the Square """

        return self.__width

    @size.setter
    def size(self, value):
        """ method to set new size of the Square """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
