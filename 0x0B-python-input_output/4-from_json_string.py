#!/usr/bin/python3

"""
Function that deserialises an object from
JSON representation.
"""

import json


def from_json_string(my_str):
    """
    A function that deserialises an object.
    my_str is in JSON representation.
    """

    return json.loads(my_str)
