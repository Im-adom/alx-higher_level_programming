#!/usr/bin/python3
"""Defining a matrix multiplication function using NumPy."""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """This function returns the multiplication of 2 matrices using Numpy.
    Args:
    m_a (a list of lists of integers or floats): First matrix
    m_b (a list of lists of integers of floats): Second matrix

    """

    return (npy.matmul(m_a, m_b))
