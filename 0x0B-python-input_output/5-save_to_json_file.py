#!/usr/bin/python3

"""
Funtion writes an object to file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a file.
    my_obj is the object.
    filename is the specified file.
    """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
