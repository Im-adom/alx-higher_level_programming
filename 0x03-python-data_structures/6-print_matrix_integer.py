#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat_row in matrix:
        print('.'.join("{:d}".format(g) for g in mat_row))
