#!/usr/bin/python3
""" module containting function to dive each element of matrix """
def matrix_divided(matrix, div):
    newMatrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for List in matrix:
        if type(List) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            newList = []
            for num in List:
                newNum = int(num / div)
                newList.append(newNum)
        newMatrix.append(newList)
    return newMatrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
