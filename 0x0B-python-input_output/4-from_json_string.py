#!/usr/bin/python3
"""function that returns an object (Python data structure)
   represented by a JSON string"""
import json


def from_json_string(my_str):
    """Function that to return python object from string

    Args:
        my_str - The JSON string to convert to an object.

    Return:
        python object.
    """
    return json.loads(my_str)
