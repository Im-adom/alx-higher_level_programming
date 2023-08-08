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
    buff = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for alphabet in text:
        buff += alphabet
        if alphabet == "." or alphabet == "?" or alphabet == ":":
            while buff[0] == " ":
                buff = buff[1:]
            print(buff)
            print()
            buff = ""
    if len(buff) != 0:
        try:
            while buff[0] == " ":
                buff = buff[1:]
        except:
            pass
        print(buff, end="")
