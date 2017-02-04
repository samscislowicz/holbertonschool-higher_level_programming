#!/usr/bin/python3
"""
Input output module
"""


def append_write(filename="", text=""):
    """
    Module to append written info
    """
    with open(filename, encoding='utf-8', mode='a') as my_file:
        return my_file.write(text)
