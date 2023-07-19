#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for col in matrix:
        ans = list(map(lambda a: a**2, col))
        newmatrix.append(ans)
    return newmatrix
