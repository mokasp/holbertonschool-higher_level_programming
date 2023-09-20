#!/usr/bin/python3
""" module containting function to print a name

    functions
    ----------
    say_my_name : prints a first and last name """


def say_my_name(first_name, last_name=""):
    """ prints a first and last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
