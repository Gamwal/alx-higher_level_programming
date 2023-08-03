#!/usr/bin/python3
"""function that writes an Object to a text file,
   using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function that to return python object from string

    Args:
        my_obj - The python object to be written.

    Return:
        Does not return.
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
