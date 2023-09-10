#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for number in my_list:
        if number <= x:
            i += 1
            print("{:d}".format(number), end="")
    print("")
    try:
        printed = i
    except TypeError:
        printed = x
    return printed


if __name__ == "__safe_print_list__":
    safe_print_list()
