#!/usr/bin/python3
""" module containg function that tests if an object is exactly an instance \
    of a specified class """


def is_same_class(obj, a_class):
    """ returns True if obj is exactly an instance of a_class \
        otherwise returns False """
    return type(obj) is a_class