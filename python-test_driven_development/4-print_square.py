#!/usr/bin/python3
""" module containting function to print a square

    functions
    ----------
    print_square : prints a square """


def print_square(size):
    """
    prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print("", end="")
    else:
        for col in range(size):
            for row in range(size + 1):
                if row == size and col < size - 1:
                    print()
                elif row < size:
                    print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
