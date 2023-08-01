#!/usr/bin/python3
"""Class definition"""


class Square:

    def __init__(self, size=0):
        """Initialization of the new square"""

    @property
    def size(self):
        """Getting the current square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        def area(self):
            return (self.__size * self.__size)
        """Returning current area square"""

        def my_print(self):
            """Printing the square with #"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
