#!/usr/bin/python3

"""
Function that returns attributes and
methods of the class
"""


def lookup(obj):
    """
    Function lookup() returns
    a list object.
    """

    return list(dir(obj))
