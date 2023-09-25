#!/usr/bin/python3
""" module containing function that reads text file and prints to stdout """


def read_file(filename=""):
    """ reads and prints to stdout a text file

        parameters
        ==========
        filename : string
            a string containing name of a textfile
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
