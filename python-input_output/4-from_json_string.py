#!/usr/bin/python3
""" module containing function that converts JSON string to object """
import json


def from_json_string(my_str):
    """ function that converts JSON string to object

    parameters
    ==========
    my_str : JSON string
        json string to convert to object
    """
    return json.loads(my_str)
