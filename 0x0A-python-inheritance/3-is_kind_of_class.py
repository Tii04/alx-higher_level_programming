#!/usr/bin/python3
""" Function that checks if class
    is instance of specified class
    or from other derivied classes.
"""


def is_kind_of_class(obj, a_class):

    """
    Function checks if obj is an instance of
    a_class or whether is was derived from class
    a_class.
    """

    if isinstance(obj, a_class):
        return True
    return False
