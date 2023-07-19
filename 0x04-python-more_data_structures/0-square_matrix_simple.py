#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()

    for nm in range(len(matrix)):
        newmatrix[nm] = list(map(lambda nm: nm**2, matrix[nm]))

    return (newmatrix)
