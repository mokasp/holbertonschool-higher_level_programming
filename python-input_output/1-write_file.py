#!/usr/bin/python3
""" module containg a function that writes a string to a test file and \
returns the number of characters written """


def write_file(filename="", text=""):
    """ function that writes text to a file and returns number of charcaters \
    written

    parameters
    ==========
    filename : string
        string containing a name of a file to write to
    text : string
        string containg text to write to file
        """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
