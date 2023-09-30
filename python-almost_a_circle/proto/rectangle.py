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

        self.__height = value

    @property
    def width(self):
        """ method to get the current width of the Rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ method to set new width of the Rectangle """

        self.__width = value

    @property
    def x(self):
        """ method to get the current X of the Rectangle """

        return self.__x

    @x.setter
    def x(self, value):
        """ method to set new X of the Rectangle """

        self.__x = value

    @property
    def y(self):
        """ method to get the current Y of the Rectangle """

        return self.__y

    @y.setter
    def y(self, value):
        """ method to set new Y of the Rectangle """

        self.__y = value
