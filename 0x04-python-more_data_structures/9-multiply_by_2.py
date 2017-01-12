#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for n in my_dict:
        new_dict[n] = my_dict[n] * 2
    return new_dict
