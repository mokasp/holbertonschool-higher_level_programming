#!/usr/bin/python3
""" module containing function that converts a string object to JSON """
import json


def to_json_string(my_obj):
    """ function that converts string object to JSON

    parameters
    ==========
    my_obj : string
        string object to convert to JSON
    """
    return json.dumps(my_obj)
