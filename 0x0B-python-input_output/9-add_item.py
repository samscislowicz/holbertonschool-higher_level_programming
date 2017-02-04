#!/usr/bin/python3
"""
Module info goes here

"""
from sys import argv
save_to_json=__import__('7-save_to_json_file').save_to_json_file
load_from_json=__import__('8-load_from_json_file').load_from_json_file


if __name__=="__main__":
    filename = "add_item.json"
    try:
        list_obj = load_from_json(filename)
    except Exception as e:
        list_obj=[]
    save_to_json(list_obj + argv[1:], filename)
