#!/usr/bin/python3

""" Module to Load, add and save python
    objects to a textfile.
"""


import json
import os
import sys

filename = "add_item.json"
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if not os.path.isfile(filename):
    obj_list = []
    save_to_json_file(obj_list, filename)

i = 1

while i < len(sys.argv):
    obj_list = load_from_json_file(filename)
    obj_list.append(sys.argv[i])
    save_to_json_file(obj_list, filename)
    i += 1
