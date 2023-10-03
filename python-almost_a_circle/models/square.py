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

    .....

    methods
    ----------
    area : int
        returns area of the Square
    display:
        prints an instance of Square
    update :
        assigns arguments to attributes
    to_dictionary :
        returns dictionary representation of Square
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

    def __str(self):
        """ returns string representation of Square """
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ method to get the current size of the Square """

        return self.__size

    @size.setter
    def size(self, value):
        """ method to set new size of the Square """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value

    def update(self, *args, **kwargs):
        """ public method that assigns arguments to attributes """
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif len(args) == 0 and kwargs is not None:
            if kwargs and len(kwargs) != 0:
                for arg in kwargs:
                    setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {'id': getattr(self, 'id'), 'x': getattr(self, 'x'),
                'size': getattr(self, 'size'), 'y': getattr(self, 'y')}
