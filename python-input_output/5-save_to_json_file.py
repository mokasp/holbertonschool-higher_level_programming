#!/usr/bin/python3
""" module containing function that writes an Object to a text file \
    as its JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file as its JSON \
        represention

    parameters
    ==========
    my_obj : any
        any python object
    filename : txt file
        a text file to write JSON object to
    """
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
