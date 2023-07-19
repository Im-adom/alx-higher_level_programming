#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    up = 0
    down = 0

    for tup in my_list:
        up += tup[0] * tup[1]
        down += tup[1]

    return (up / down)
