#!/usr/bin/python3
""" module containg function that tests if an object is an instance of a \
    specified class """


def is_kind_of_class(obj, a_class):
    """ returns True if obj is an instance of a_class or a class inherited \
        from a_class, otherwise returns False """
    return isinstance(obj, a_class)
