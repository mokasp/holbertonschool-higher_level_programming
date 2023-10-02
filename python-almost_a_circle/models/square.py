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

    def __str__(self):
        """ returns string representation of Square """
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.height)
