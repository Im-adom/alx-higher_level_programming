#!/usr/bin/python3
"""Defines a rectangle class that inherits from a
BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This represents a rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializing a new Rectangle.
        Args:
        width (int): Width of new Rectangle.
        height (int): Height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
