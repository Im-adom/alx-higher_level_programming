#!/usr/bin/python3
"""Defines a text-file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """This inserts a line of text to a file."""

    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as g:
        g.write(txt)
