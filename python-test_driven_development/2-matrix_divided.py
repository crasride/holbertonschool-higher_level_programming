#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Funtion Divide all elements of a matrix
    """
    new_matrix = []
    new_matrix2 = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of" +
                        "integers/floats")
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
    for x in row:
        if type(x) is not int and type(x) is not float:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
    for row in matrix:
        try:
            if len(row) != len(matrix[1]):
                raise TypeError("Each row of the matrix must have the same " +
                                "size")
        except IndexError:
            break

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        for x in row:
            new_matrix2.append(round(x / div, 2))

            new_matrix.append(new_matrix2)
            new_matrix2 = []

    return new_matrix
