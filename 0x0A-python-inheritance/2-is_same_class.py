#!/usr/bin/python3
"""
Function that if object is instance of
specified class.
"""


def is_same_class(obj, a_class):
    """
    Function checks if the object is exactly
    an instance of the specified class.
    If is instance, true is returned, otherwise
    False.
    """

    if type(obj) == a_class:
        return True
    return False
