#!/usr/bin/python3
""" module that contains function that returns the dictionary description \
    for JSON serialization of an object """


def class_to_json(obj):
    """ function that returns the dictionary description for JSON \
        serialization of an object"""
    return obj.__dict__
