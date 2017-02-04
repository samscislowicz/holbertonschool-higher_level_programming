#!/usr/bin/python3
import json
"""
input output module
"""


def save_to_json_file(my_obj, filename):
    """
    function that saves file as json object
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
