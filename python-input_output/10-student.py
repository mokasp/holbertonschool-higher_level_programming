#!/usr/bin/python3
""" module containing a Class used to represent a Student """


class Student():
    """ class representing a Student

    attributes
    ==========
    first_name : string
        first name of student
    last_name : string
        last name of student
    age : int
        age of student

    methods
    =======
    to_json : none
        returns dict representation of a student instance
    """
    def __init__(self, first_name, last_name, age):
        """ initializes class Student

        parameters
        ==========
        first_name : string
            first name of student
        last_name : string
            last name of student
        age : int
            age of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public instance method that returns the dictionary description \
        for JSON serialization of an object

        parameters
        ==========
        attrs : list
            list of attributes to print as dict
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in range(len(attrs)):
                try:
                    new_dict[attrs[i]] = self.__dict__[attrs[i]]
                except KeyError:
                    pass
            return new_dict
