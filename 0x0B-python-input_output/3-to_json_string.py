#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Function that to return string representation

    Args:
        my_obj - The object to convert to a string.

    Return:
        string representation of an object.
    """
    return json.dumps(my_obj)
