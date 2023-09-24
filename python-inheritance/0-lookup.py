#!/usr/bin/python3
""" module containing function that retrieves list of available attributes \
    and methods of an object

    functions
    ----------
    lookup : any object
        retrieves list of available attributes and methods of an object
    """


def lookup(obj):
    """ retrieves list of available attributes and methods of an object """
    return dir(obj)