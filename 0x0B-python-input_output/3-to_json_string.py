#!/usr/bin/python3

"""
Function that returns JSON representation of object.
"""


import json


def to_json_string(my_obj):
    """
    Function returns JSON representation of object.
    my_obj is of type str.
    """

    return json.dumps(my_obj)
