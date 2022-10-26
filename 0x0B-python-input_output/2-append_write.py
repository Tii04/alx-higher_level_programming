#!/usr/python3

"""
Function appends text to a file
"""


def append_write(filename="", text=""):
    """
    Function that appends text to any valid file.
    utf-8 encoding.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.append(text)
