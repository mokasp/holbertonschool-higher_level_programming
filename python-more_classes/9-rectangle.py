#!/usr/bin/python3
"""
a module containing a Rectangle
"""


class Rectangle:
    """
    a class used to represent a Rectangle

    .....

    attributes
    ----------
    width : int, optional
        width of the Rectangle
    height : int, optional
        heigth of the Rectangle

    .....

    methods
    ----------
    area : int
        returns area of the Rectangle
    perimeter : int
        returns perimeter of the Rectangle

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns string representation of the Rectangle """
        my_list = []
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        else:
            for col in range(self.height):
                for row in range(self.width + 1):
                    if row == self.width and col < self.height - 1:
                        my_list.append("\n")
                    elif row < self.width:
                        my_list.append(self.print_symbol)
            for item in my_list:
                string += "{}".format(item)
            return string

    def __repr__(self):
        """ returns representation of the Rectangle """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ deletes object Rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """ method to get the current width of the Rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ method to set new width of the Rectangle """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ method to get area of the Rectangle """

        return self.width * self.height

    def perimeter(self):
        """ method to get parameter of the Rectangle """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the largest Rectangle by area """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a Square instance of Rectangle """

        return cls(size, size)
