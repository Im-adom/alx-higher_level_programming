#!/usr/bin/python3
def remove_char_at(str, n):
    gee = ""
    a = 0
    for c in str:
        if a != n:
            gee += c
        a += 1
        return gee
