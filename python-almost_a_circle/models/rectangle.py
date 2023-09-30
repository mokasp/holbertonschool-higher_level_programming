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

        if self.hw_validator("height", value):
            self.__height = value

    @property
    def width(self):
        """ method to get the current width of the Rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ method to set new width of the Rectangle """

        if self.hw_validator("width", value):
            self.__width = value

    @property
    def x(self):
        """ method to get the current X of the Rectangle """

        return self.__x

    @x.setter
    def x(self, value):
        """ method to set new X of the Rectangle """

        if self.xy_validator("x", value):
            self.__x = value

    @property
    def y(self):
        """ method to get the current Y of the Rectangle """

        return self.__y

    @y.setter
    def y(self, value):
        """ method to set new Y of the Rectangle """

        if self.xy_validator("y", value):
            self.__y = value

    def hw_validator(self, name, value):
        """ Instance Method that validates whether a value is a positive \
        integer 
        
        parameters
        ----------
        name : string
            name of value
        value : integer
            positive integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > than 0".format(name))
        return True

    def xy_validator(self, name, value):
        """ Instance Method that validates whether a value is a positive \
        integer 
        
        parameters
        ----------
        name : string
            name of value
        value : integer
            positive integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be <= than 0".format(name))
        return True
