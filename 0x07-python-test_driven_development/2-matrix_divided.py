#!/usr/bin/python3
"""
Defines a function that divides the numbers of a matrix.
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_t = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg)

    leng = 0
    msg_s = "Each row of the matrix must have the same size"

    for elem in matrix:
        if not elem or not isinstance(elem, list):
            raise TypeError(msg_t)

        if leng != 0 and len(elem) != leng:
            raise TypeError(msg_s)

        for num in elem:
            if not type(num) in (int, float):
                raise TypeError(msg_t)

        leng = len(elem)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
