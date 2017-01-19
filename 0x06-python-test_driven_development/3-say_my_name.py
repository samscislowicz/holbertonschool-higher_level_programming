#!/usr/bin/python3
"""
This module defines the say_my_name function printing out the first_name and last_name
"""
def say_my_name(first_name, last_name=""):
    """ Prints 2 strings as first and last name.

    first_name and last_name must be strings.
    """
    if type(first_name) != str:
        raise TypeError ("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError ("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
