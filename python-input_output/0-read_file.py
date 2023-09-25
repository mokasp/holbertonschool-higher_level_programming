#!/usr/bin/python3
""" module containing function that reads text file and prints to stdout """


def read_file(filename=""):
    """ reads and prints to stdout a text file

        parameters
        ==========
        filename : string
            a string containing name of a textfile
    """
    if filename == "":
        pass
    else:
        with open(filename, "r", encoding="utf-8") as f:
            read_data = f.read()
        print(read_data)
