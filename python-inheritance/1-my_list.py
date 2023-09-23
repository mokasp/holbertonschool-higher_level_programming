#!/usr/bin/python3
""" module containing a class that inherits from another class
"""


class MyList(list):
    """ class inherited from list class

    methods
    ----------
    print_sorted: None
        prints sorted list
    """

    def print_sorted(self):
        print(sorted(list(self)))
