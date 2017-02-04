#!/usr/bin/python3
"""
Input/ output module
"""


def number_of_lines(filename=""):
    """
    Number of lines in a file function
    """
    with open(filename, encoding="utf-8") as my_file:
        l = 0
        for line in my_file:
            l += 1
        return l
