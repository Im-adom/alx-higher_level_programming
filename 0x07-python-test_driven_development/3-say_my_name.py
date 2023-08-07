#!/usr/bin/python3
"""Defining a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """This function prints a name.


    Args:
    first_name: prints the first name.
    last_name: prints the last name.

    Raises:
    TypeError: if first_name or last_name is not a strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
