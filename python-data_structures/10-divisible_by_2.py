#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [x % 2 == 0 for x in my_list]
    return new_list


if __name__ == "__divisible_by_2__":
    divisible_by_2()
