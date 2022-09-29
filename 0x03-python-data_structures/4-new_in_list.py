#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        c = my_list.copy()
        return c
    if idx > len(my_list) - 1:
        c = my_list.copy()
        return c
    c = my_list.copy()
    c.pop(idx)
    c.insert(idx, element)
    return c
