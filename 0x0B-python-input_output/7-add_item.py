#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg = list(sys.argv[1:])

try:
    old = load_from_json_file('add_item.json')
except Exception:
    old = []

old.extend(arg)
save_to_json_file(old, 'add_item.json')
