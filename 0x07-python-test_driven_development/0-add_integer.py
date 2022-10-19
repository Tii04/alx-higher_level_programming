#!/usr/bin/python3

""" Defines a function that will add numbers
    Function takes floats or integers as arguments
    and returns a number of type int.
    If the function is not given int or float, TyperError is raised.
"""


def add_integer(a, b=98):
    """ Arguments: floats and integers.
    Return: typecasted to int.
    Otherwise, TyperError raised"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a + b))
