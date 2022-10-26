#!/usr/python3

"""
Function writes to a file
"""


def write_file(filename="", text=""):
    """
    Function that writes text to any valid file.
    utf-8 encoding.
    """

    with open(filename, 'w') as f:
        return f.write(text)
