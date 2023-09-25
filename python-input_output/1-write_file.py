#!/usr/bin/python3
""" module containg a function that writes a string to a test file and \
returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)