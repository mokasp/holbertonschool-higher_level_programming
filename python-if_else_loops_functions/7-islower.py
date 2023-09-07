#!/usr/bin/python3
def islower(c):
    lowercase = range(97, 123)
    for letter in lowercase:
        if ord(c) == letter:
            return True
    return False
