#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    print("\n".join([" ".join(["{:d}".format(mat_numb)
        for mat_numb in g]) for g in matrix]))
