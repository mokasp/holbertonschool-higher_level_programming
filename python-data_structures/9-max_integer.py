#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maximum = my_list[0]
        for number in my_list:
            if number > maximum:
                maximum = number
        return maximum


if __name__ == "__max_integer__":
    max_integer()
