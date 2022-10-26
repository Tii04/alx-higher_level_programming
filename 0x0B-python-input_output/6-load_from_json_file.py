#!/usr/bin/python3

"""
Function that creates object from JSON file.
"""

import json


def load_from_json_file(filename):
    """
    function creates object from json file.
    Filename is the json file.
    """

    with open(filename) as f:
        return json.load(filename)
