#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listof_keys = list(a_dictionary.keys())

    for val_in_dic in listof_keys:
        if value == a_dictionary.get(val_in_dic):
            del a_dictionary[val_in_dic]

    return a_dictionary
