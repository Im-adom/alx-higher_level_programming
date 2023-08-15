#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """This represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This gets the dictionary presentation of Student.

        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved"""

        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {g: getattr(self, g) for g in attrs if hasattr(self, g)}
        return self.__dict__

    def reload_from_json(self, json):
        """This replaces all the attributes of the Student"""
        for attr in json:
            self.__dict__[attr] = json[attr]
