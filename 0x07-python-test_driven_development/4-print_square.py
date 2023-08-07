#!/usr/bin/python3
"""Defining a function that prints a square."""


def print_square(size):
    """This prints a square with '#'.

    Args:
    size (int): the size length of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        [print("#", end="") for b in range(size)]
        print("")
