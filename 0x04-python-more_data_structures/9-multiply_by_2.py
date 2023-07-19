#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dic = a_dictionary.copy()
    n_keys = list(multi_dic.keys())

    for g in n_keys:
        multi_dic[g] *= 2

    return (multi_dic)
