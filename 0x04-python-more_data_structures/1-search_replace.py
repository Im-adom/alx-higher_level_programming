#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for item in my_list:
        if item == search:
            newlist.append(replace)
        else:
            newlist.append(item)
    return newlist
