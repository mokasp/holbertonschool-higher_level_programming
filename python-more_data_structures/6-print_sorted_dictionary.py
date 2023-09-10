#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items()))
    for item in new_dict:
        print("{}: {}".format(item, new_dict[item]))


if __name__ == "__print_sorted_dictionary__":
    print_sorted_dictionary()
