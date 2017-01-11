#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for next_char in my_string:
        if next_char is not 'c' and next_char is not 'C':
            new_string += next_char
    return new_string
