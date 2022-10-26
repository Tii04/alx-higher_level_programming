#!/usr/bin/python3

"""
Function that reads a file
"""


def read_file(filename=""):
    """ Function that reads whatever valid
    file that is inserted as parameter. Encoding is UTF - 8.
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
