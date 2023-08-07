#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0)
    """Initializing the new rectangle.
    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.

        """
    self.width = width
    self.height = height

    @property
    def width(self):
        """Get/set the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return((self.__width * 2) + (self.__height * 2))
