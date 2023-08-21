#!/usr/bin/python3
"""This defines the class called Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This represents a Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the new Square."""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """To get or set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This updates the Square."""
        if args and len(args) != 0:
            g = 0
            for arg in args:
                if g == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif g == 1:
                    self.size = arg
                elif g == 2:
                    self.x = arg
                elif g == 3:
                    self.y = arg
                g += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = b
                elif a == "size":
                    self.size = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """This returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """This returns the print and string representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
