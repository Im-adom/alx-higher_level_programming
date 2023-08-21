#!/usr/bin/python3
"""Defines a class called Base."""
import json
import csv
import random
import turtle


class Base:
    """This represents the base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dicts."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This writes the JSON serialization of a list of objects
        to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [j.to_dictionary() for j in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """This returns the deserialization of a JSON string"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This returns a class instantied from a dictionary of attributes."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dic_cls = cls(1, 1)
            else:
                dic_cls = cls(1)
            dic_cls.update(**dictionary)
            return dic_cls

    @classmethod
    def load_from_file(cls):
        """This returns a list of classes instantiated from
        a file of JSON strings."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This writes the CSV serialization of a list of objects to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This returns a list of classes instantiated from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([a, int(b)] for a, b in dic.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This draws Rectangles and Squares using the turtle module."""
        s = turtle.Screen()
        t = turtle.Turtle()
        col = ["pink", "purple", "white"]
        turtle.bgcolor("black")
        t.pensize(3)
        shapes = list_rectangles + list_squares
        for shape in shapes:
            t.pencolor(cl[random.randint(0, 2)])
            t.up()
            t.goto(shape.x, shape.y)
            t.down()
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)

        s.exitonclick()
