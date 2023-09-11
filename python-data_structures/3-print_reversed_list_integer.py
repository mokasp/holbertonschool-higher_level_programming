#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list.copy()
    for number in reversed(new_list):
        print("{:d}".format(number))


if __name__ == "__print_reversed_list_integer__":
    print_reversed_list_integer()
