#!/usr/bin/python3

def rectangle(height, width):
    rect = []
    for i in range(0, height):
        for w in range(0, width):
            rect.append("#")
        if i != height -1:
            rect.append("\n")
    return ("".join(rect))
