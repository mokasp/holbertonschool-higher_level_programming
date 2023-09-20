#!/usr/bin/python3
""" module containting function to indent a text

    functions
    ----------
    text_indentation : indent a text """


def text_indentation(text):
    """
    indent a text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        newString = ""
        i = 0
        for x in text:
            i += 1
            newString += x
            if x == "." or x == "?" or x == ":":
                newString += "\n\n"
                newString = newString.strip()
                print("{}".format(newString))
                print()
                newString = ""
            elif i == len(text):
                newString = newString.strip()
                print("{}".format(newString), end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
