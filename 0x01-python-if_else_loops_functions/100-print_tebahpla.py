#!/usr/bin/python3
for g in range(122, 96, -1):
    if g % 2 != 0:
        g = g - 32
        print("{}".format(chr(g)), end="")
