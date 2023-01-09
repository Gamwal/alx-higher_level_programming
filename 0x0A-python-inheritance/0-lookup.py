#!/usr/bin/python3
def lookup(obj):
    """function that returns all the methods
    and attributes of an object.

    Args:
        obj (object): object in question.

    Returns:
        list: list of all object attribs and methods

    """
    return dir(obj)
