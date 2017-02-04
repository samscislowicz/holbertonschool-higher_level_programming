#!/usr/bin/python3
"""
Input output module
"""


def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a text file and prints
    """
    with open(filename, encoding="utf-8") as my_file:
        if nb_lines <= 0:
            print(my_file.read(), end='')
        else:
            for i in range(nb_lines):
                print(my_file.readline(), end='')
