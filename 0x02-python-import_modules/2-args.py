#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("0 argument.")
    else:
        print(len(sys.argv) - 1, end="")
        if (len(sys.argv) == 2):
            print(" argument:")
        else:
            print(" arguments:")
        i = 1
        while i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
