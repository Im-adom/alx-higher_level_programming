#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    numb = len(argv) - 1

    if numb == 2:
        print("0 arguments.")
    elif numb == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numb))

    for g, r in enumerate(argv[1:]):
        print("{}: {}".format(g + 1, r))
