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

    .....

    methods
    ----------
    area : int
        returns area of the Rectangle
    display:
        prints an instance of Rectangle
    update :
        assigns arguments to attributes
    to_dictionary :
        returns dictionary representation of Rectangle

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

    def area(self):
        """ method to get area of the Rectangle """

        return self.width * self.height

    def display(self):
        """ prints the Rectangle """

        for row in range(self.__y + self.__height):
            if row < self.__y:
                print()
            else:
                for col in range(self.__x + self.__width):
                    if col < self.__x:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    def __str__(self):
        """ returns string representation of Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ public method that assigns arguments to attributes """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif len(args) == 0:
            if kwargs and len(kwargs) != 0:
                for arg in kwargs:
                    setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {'x': getattr(self, 'x'), 'y': getattr(self, 'y'),
                'id': getattr(self, 'id'), 'height': getattr(self, 'height'),
                'width': getattr(self, 'width')}
