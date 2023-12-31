#!/usr/bin/python3
""" module containing a class BaseGeometry """


class BaseGeometry():
    """ a class used to represent BaseGeometry

    methods
    ---------------
    area : returns area of instance
    """
    def area(self):
        """ returns area of an instance """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
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
            raise ValueError("{} must be greater than 0".format(name))
        return True
