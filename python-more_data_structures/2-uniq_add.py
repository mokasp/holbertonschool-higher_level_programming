#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_list = list(set(my_list))
    for number in new_list:
        result += number
    return result


if __name__ == "__uniq_add__":
    uniq_add()
