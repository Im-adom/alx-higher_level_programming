#!/usr/bin/python3
"""Defining a text-indentation function"""


def text_indentation(text):
    """ This function prints a text with 2 new
    lines after each of the characrters: '.', ':' and '?'.

    Args:
    text: this must be a string.

    Raise:
    TypeError: If the text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    g = 0
    while g < len(text) and text[g] == ' ':
        g += 1

    while g < len(text):
        print(text[g], end="")
        if text[g] == "\n" or text[g] in ".?:":
            print("\n")
        g += 1
        while g < len(text) and text[g] == ' ':
            g += 1
        continue
    g += 1
