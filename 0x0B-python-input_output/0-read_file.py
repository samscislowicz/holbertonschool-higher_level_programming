#!/usr/bin/python3
def read_file(filename=""):
    """
    Read a file with a with statement
    """
    with open("my_file_0.txt", mode="r", encoding="utf-8") as my_file:
        print(my_file.read())
