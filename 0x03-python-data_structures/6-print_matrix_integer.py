#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat_row in matrix:
        for numb in mat_row:
            print("{:d}".format(numb, end="  "))
        print()
