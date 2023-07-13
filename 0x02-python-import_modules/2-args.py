#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count_args = len(sys.argv) - 1
    if count_args == 0:
        print("0 arguments")
    elif count_Args == 1:
        print("1 argument")
    else:
        print("{} arguments: ".format(count_args))
        for g in range(count_args):
            print("{}: {}".format(g + 1, sys.argv[g + 1]))
