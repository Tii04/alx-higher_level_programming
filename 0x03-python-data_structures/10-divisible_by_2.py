#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boolean = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            boolean[count] = True
        else:
            boolean[count] = False
    return boolean
