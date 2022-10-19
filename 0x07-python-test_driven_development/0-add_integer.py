#!/usr/bin/python3

""" Defines a function that will add numbers"""


def add_integer(a, b=98):
    """
    Function takes both floats and integers but the return
    is typecasted to int.

    TypeError raised if a or b is not an int or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a + b))
