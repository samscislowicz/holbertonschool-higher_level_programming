#!/usr/bin/python3
"""
This module holds the function add_integer that adds two integers
"""


def add_integer(a, b):
    """Returns a + b as int.

    a and b must be integers or floats.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a + b)
