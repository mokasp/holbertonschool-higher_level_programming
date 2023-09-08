#!/usr/bin/python3
def no_c(my_string):
    removeC = {99: None, 67: None}
    return my_string.translate(removeC)


if __name__ == "__no_c__":
    no_c()
