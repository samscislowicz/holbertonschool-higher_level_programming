#!/usr/bin/python3
"""
Input output module
"""


def write_file(filename="", text=""):
    """
    File to open file and write to it
    """
    with open(filename, encoding='utf-8', mode='w') as my_file:
        return my_file.write(text)
