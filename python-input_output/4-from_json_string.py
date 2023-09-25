#!/usr/bin/python3
""" module containing function that converts a string object to JSON """
import json


def from_json_string(my_str):
    """ function that converts string object to JSON

    parameters
    ==========
    my_str : string
        not really sure yet
    """
    return json.loads(my_str)
