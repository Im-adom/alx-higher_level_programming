#!/usr/bin/python3
"""Class definition"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the new square
        Arguments:
            size (int): size of new square.
            position (int, int): position of new square.
            """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        def area(self):
            return (self.__size * self.__size)
        """Returning current area square"""

        def my_print(self):
            """Printing the square with #"""
            if self.__size == 0:
                print("")
                return
        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for z in range(0, self.__position[0])]
            [print("#", end="") for y in range(self.__size)]
            print("")
