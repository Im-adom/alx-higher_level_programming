#!/usr/bin/python3
"""Defines a function that reads the content of a file"""


def read_file(filename=""):
    """Printing the content of a text file to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
