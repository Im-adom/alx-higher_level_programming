#!/usr/bin/python3
"""Defining an integer adding function"""


def add_integer(a, b=98):

    """This function returns the addition of two integers a and b.

    Typecast float arguments to int before performing addition.

    Raise:
    TypeError: if a or b is not an integer and not a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
