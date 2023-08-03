#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attrib_name, attrib_value):
    """Function to add new attribute if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attrib_name, attrib_value)
