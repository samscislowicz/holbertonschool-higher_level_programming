#!/usr/bin/python3
"""
Input output module
"""


def read_file(filename=""):
    """
    Read a file with a with statement
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
