#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        new_dict = a_dictionary.pop(key)
    return a_dictionary


if __name__ == "__simple_delete__":
    simple_delete()
