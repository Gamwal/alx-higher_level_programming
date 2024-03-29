#!/usr/bin/python3
"""script that adds all arguments to a Python list,
   and then save them to a file"""
import sys
import os
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    if not os.path.exists('add_item.json'):
        with open('add_item.json', 'w', encoding='utf-8'):
            pass
    try:
        my_obj = load_from_json_file('add_item.json')
        if my_obj == []:
            my_obj = sys.argv[1:]
        else:
            my_obj += sys.argv[1:]
        save_to_json_file(my_obj, 'add_item.json')
    except json.decoder.JSONDecodeError:
        my_obj = sys.argv[1:]
        save_to_json_file(my_obj, 'add_item.json')
