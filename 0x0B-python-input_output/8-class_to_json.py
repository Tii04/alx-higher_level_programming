#!/usr/bin/python3
"""
Function that returns dictionary description for
JSON objects.
"""


def class_to_json(obj):
    """
    Function returns dictionary description for json
    objects.
    """

    return obj.__dict__
