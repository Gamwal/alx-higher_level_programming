#!/usr/bin/python3
"""
function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) 
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """class to json function"""
    my_obj =  json.dumps(obj.__dict__())
    return json.loads(my_obj)
