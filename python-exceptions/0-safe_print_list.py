#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for number in my_list:
        if number <= x:
            print("{:d}".format(number), end="")
    print("")
    try:
        printed = number
    except TypeError:
        printed = x
    return printed


if __name__ == "_safe_print_list__":
    safe_print_list()
