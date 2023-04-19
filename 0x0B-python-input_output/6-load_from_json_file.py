#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Function that to return python object from file

    Args:
        filename - The file to get the JSON string from.

    Return:
        Does not return.
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        myFile.read(filename)
        return json.loads(myFile)
