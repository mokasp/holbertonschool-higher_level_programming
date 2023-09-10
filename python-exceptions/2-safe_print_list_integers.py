#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    i = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except ValueError:
            next
        except TypeError:
            next
    print("")
    try:
        printed = j
    except TypeError:
        printed = x
    return printed


if __name__ == "__safe_print_list_integers__":
    safe_print_list_integers()
