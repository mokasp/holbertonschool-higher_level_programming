#!/usr/bin/python3
""" module containting function to dive each element of matrix """
def matrix_divided(matrix, div):
    for aList in matrix:
        if type(aList) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            for col in aList:
                for row in col:
                    matrix[col][row] / 2
    return matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
