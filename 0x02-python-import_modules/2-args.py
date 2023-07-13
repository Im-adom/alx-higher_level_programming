#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    c_arg = sys.argv
    size = len(c_arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for a in range(1, size + 1):
            print("{}: {}".format(a, c_arg[a]))
        elif size == 0:
            print("{} arguments.".format(size))
        else:
            print("{} argument:".format(size))
            print("{}: {}".format(size, c_arg[1]))
