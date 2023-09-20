#!/usr/bin/python3
""" module to add two integers

    functions
    ----------
    add_integer : returns sum of two integers """


def add_integer(a, b=98):
    """
    adds two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    num = int(a) + int(b)
    if num == float('inf') or num == -float('inf'):
        num = 0
    return num


if __name__ == "__main__":
    import doctest
    doctest.testmod()
