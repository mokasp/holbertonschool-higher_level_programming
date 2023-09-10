#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    return dict(zip(new_dict.keys(), map(lambda x: x*2, new_dict.values())))


if __name__ == "__multiply_by_2__":
    multiply_by_2()
