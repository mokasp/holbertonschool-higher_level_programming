#!/usr/bin/python3
""" module containg a function that returns a matrix representation of \
    pascals triangle"""


def pascal_triangle(n):
    """ function that returns a matrix representation of \
    pascals triangle"""
    solved = []
    solved = []
    if n <= 0:
        return solved
    for row in range(n):
        new_row = [1]
        for col in range(1, row + 1):
            new_cell = new_row[col - 1] * float(row + 1 - col) / col
            new_row.append(int(new_cell))
        solved .append(new_row)
    return solved
