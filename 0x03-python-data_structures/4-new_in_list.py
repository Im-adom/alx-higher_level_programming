#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = len(my_list)

    cpy = my_list[:]
    if 0 <= idx < new:
        cpy[idx] = element
    return (cpy)
