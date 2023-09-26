#!/usr/bin/python3
""" module containing function that creates an Object from a JSON file """
import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file

    parameters
    ==========
    filename : json file
        a JSON file to read from
    """
    with open(filename, "r") as read_file:
        return json.load(read_file)

