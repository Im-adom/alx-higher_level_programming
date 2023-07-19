#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_int = set()
    total_add = 0

    for n in my_list:
        if n not in set_int:
            total_add += n
            set_int.add(n)
    return total_add
