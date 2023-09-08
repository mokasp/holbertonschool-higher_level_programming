#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for item in sublist:
            print("{:d}".format(item), end=" ")
        print("")
