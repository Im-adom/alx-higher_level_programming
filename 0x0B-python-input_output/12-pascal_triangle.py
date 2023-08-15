#!/usr/bin/python3
"""Defines Pascal's triangle function"""


def pascal_triangle(n):
    """Pascal's triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        t = triangle[-1]
        temp = [1]
        for x in range(len(t) - 1):
            temp.append(t[x] + t[x + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
