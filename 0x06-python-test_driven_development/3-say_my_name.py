#!/usr/bin/python3
"""
This is the say_my_name module.
This is to print out the first and last names that is typed in.
"""


def say_my_name(first_name, last_name=""):
    """ Prints 2 strings as first and last name.

    first_name and last_name must be strings.
    """
    if isinstance(first_name) != str:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
