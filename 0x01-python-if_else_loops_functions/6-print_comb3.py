#!/usr/bin/python3

for i in range(0, 10):
    for x in range(0, 10):
        if i >= x:
            continue
        elif i == 8 and x == 9:
             print("{}{}".format(i, x), end="")
        else:
             print("{}{}, ".format(i, x), end="")
