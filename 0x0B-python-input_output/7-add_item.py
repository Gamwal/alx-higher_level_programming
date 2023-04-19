#!/usr/bin/python3
"""script that adds all arguments to a Python list,
   and then save them to a file"""


import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if not os.path.exists('add_item.json'):
    with open('add_item.json', 'w', encoding='utf-8'):
        pass

save_to_json_file(sys.argv[1:], 'add_item.json')
load_from_json_file('add_item.json')
