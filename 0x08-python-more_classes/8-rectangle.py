#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """This represents a rectangle

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_sympbol : The symbol for the string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0)
    """Initializing the new rectangle.
    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with greater area.
        Args:
        rect_1 (Rectangle): The first Rectangle.
        rect_2 (Rectangle): Second Rectangle.

        Raise:
        TypeError: if either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Return a printable presentation of the Rectangle.

        This represents a rectangle printed with the '#' character.
        """
    if self.__width == 0 or self.__height == 0:
        return ("")

    r_tangle = []
    for r in range(self.__height):
        [r_tangle.append(str(self.print_symbol)) for t in range(self.__width)]
        if r != self.__height - 1:
            r_tangle.append("\n")
            return ("".join(r_tangle))

    def __repr__(self):
        """Return a string representation of the Rectangle."""
        r_tangle = "Rectangle(" + str(self.__width)
        r_tangle += ", " + str(self.__heigh) + ")"
        return (r_tangle)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
