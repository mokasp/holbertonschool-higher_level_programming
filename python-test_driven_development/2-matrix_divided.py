#!/usr/bin/python3
""" module containting function to divide each element of matrix

    functions
    ----------
    matrix_divided : divides matrix by a given number """


def matrix_divided(matrix, div):
    """
    divides matrix by a given number
    """
    tooLong = "matrix must be a matrix (list of lists) of integers/floats"
    if len(set(map(len, matrix))) not in (0, 1):
        raise TypeError("Each row of the matrix must have the same size")
    newMatrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for List in matrix:
        if type(List) is not list:
            raise TypeError(tooLong)
        else:
            newList = []
            for num in List:
                if type(num) is not int:
                    raise TypeError(tooLong)
                newNum = int(num / div)
                newList.append(newNum)
        newMatrix.append(newList)
    return newMatrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
