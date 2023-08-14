#!/usr/bin/python3
"""Defines a class called BaseGeometry."""


class BaseGeometry:
    """This is the base geometry class"""

    def area(self):
        """This has not been implemeted yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates a parameter as integer.
    Args:
    value (int): Parameter to validate.
    name (str): Parameter to validate.
    Raises:
    TypeError: if value is not an integer.
    ValueError: if value <= 0.
    """
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
