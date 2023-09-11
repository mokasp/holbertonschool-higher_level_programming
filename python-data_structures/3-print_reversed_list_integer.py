#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for number in list(reversed(my_list)):
        print("{:d}".format(number))


if __name__ == "__print_reversed_list_integer__":
    print_reversed_list_integer()
