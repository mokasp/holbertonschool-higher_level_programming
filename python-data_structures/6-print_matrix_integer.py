#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        length = len(sublist)
        i = 0
        for item in sublist:
            i += 1
            if i < length:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item), end="")
        print("")


if __name__ == "__print_matrix_integer__":
    print_matrix_integer()
