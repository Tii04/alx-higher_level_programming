#!/usr/bin/python3

""" A function that prints last and first name."""

def say_my_name(first_name, last_name=""):
    """
    Arguments: 
    first_name of type str.
    last_name of type str.

    if not of type string, TypeError raised.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
