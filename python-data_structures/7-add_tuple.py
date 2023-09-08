#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        newTuple_a = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        newTuple_a = (0, 0)
    else:
        newTuple_a = tuple_a
    if len(tuple_b) == 1:
        newTuple_b = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        newTuple_b = (0, 0)
    else:
        newTuple_b = tuple_b
    newTup = ((newTuple_a[0] + newTuple_b[0]), (newTuple_a[1] + newTuple_b[1]))
    return newTup


if __name__ == "__add_tuple__":
    add_tuple()
