#!/usr/bin/python3
def no_c(my_string):
    new = [g for g in my_string if g != 'c' and g != 'C']
    return ("".join(new))
