#!/usr/bin/python3
"""Defining a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """The multiplication of two matrices.

    Args:
    m_a (a list of lists of integers and floats.): First matrix
    m_b (a list of lists of integers and floats.): Second matrix

    Raises:
    TypeError: If m_a or m_b is not a list of list(ints/float).
    TypeError: If m_a or m_b is empty.
    TypeError: If m_a or m_b has different sizes of rows.
    ValueError: If m_a and m_b can't be multiplied.

    Returns:
    A new matrix that shows the multiplication of m_a and m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    b_invert = []
    for i in range(len(m_b[0])):
        n_row = []
        for g in range(len(m_b)):
            n_row.append(m_b[g][i])
        b_invert.append(n_row)

    new_mat = []
    for row in m_a:
        n_row = []
        for col in b_invert:
            prod = 0
            for p in range(len(b_invert[0])):
                prod += row[p] * col[p]
            n_row.append(prod)
        new_mat.append(n_row)

    return new_mat
