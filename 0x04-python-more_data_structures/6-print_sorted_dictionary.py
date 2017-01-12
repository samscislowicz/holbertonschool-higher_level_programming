#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for n in sorted(my_dict.keys()):
        print("{}: {}".format(n, my_dict[n]))
