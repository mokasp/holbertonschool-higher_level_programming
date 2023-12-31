#!/usr/bin/python3
""" module containing function that tests if object is an instance of a \
    class that inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """ returns True if obj is an instance of a class that inherited \
        (directly or indirectly) from the specified class, otherwise returns \
        False """
    if type(obj) is not a_class:
        if issubclass(type(obj), a_class):
            return True
        else:
            return False
    else:
        return False
