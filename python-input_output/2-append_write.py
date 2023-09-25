#!/usr/bin/python3
""" module containg a function that appends a string to a test file and \
returns the number of characters added """


def append_write(filename="", text=""):
    """ function that appends text to a file and returns number of charcaters \
    added

    parameters
    ==========
    filename : string
        string containing a name of a file to append to
    text : string
        string containg text to append to file
        """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
