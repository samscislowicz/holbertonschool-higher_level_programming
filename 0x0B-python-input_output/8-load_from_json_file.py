#!/usr/bin/python3
import json
"""
input output module
"""


def load_from_json_file(filename):
    """
    function to load from json object
    """
    with open(filename, 'r') as f:
        return json.load(f)
