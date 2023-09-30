#!/usr/bin/python3
""" module containing a class Rectangle inherited from Base """
from models.base import Base


class Rectangle(Base):
    """
    a class used to represent a Rectangle

    .....

    attributes
    ----------
    width : int, optional
        width of the Rectangle
    height : int, optional
        heigth of the Rectangle
    x : int, optional
        x axis
    y : int, optional
        y axis

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructs all attributes of the Rectangle

        .....

        parameters
        ----------
        width : int, optional
            width of the Rectangle
        height : int, optional
            heigth of the Rectangle
        x : int, optional
            x axis
        y : int, optional
            y axis
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def height(self):
        """ method to get the current height of the Rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ method to set new height of the Rectangle """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ method to get the current width of the Rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ method to set new width of the Rectangle """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def x(self):
        """ method to get the current X of the Rectangle """

        return self.__x

    @x.setter
    def x(self, value):
        """ method to set new X of the Rectangle """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ method to get the current Y of the Rectangle """

        return self.__y

    @y.setter
    def y(self, value):
        """ method to set new Y of the Rectangle """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
