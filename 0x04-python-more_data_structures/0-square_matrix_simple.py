#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    col = len(matrix[0])
    row = len(matrix)

    matrix_square = [[0] * col for _ in range(row)]

    for x in range(row):
        for y in range(col):
            matrix_square[x][y] = matrix[x][y] ** 2
    return matrix_square
