#!/usr/bin/python3
"""
Module comments
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function to insert a line of text into a file after a specific string.
    """
    if new_string[-1] == '\n':
        new_string = new_string[:-1]
    with open(filename, 'r', encoding='utf-8') as f:
        temp_list = []
        a = f.read().split('\n')
        for line in a:
            temp_list.append(line)
            if search_string in line:
                temp_list.append(new_string)
    with open(filename, 'w+', encoding='utf-8') as f:
        f.write("\n".join(temp_list))
