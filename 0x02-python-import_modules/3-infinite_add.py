#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    if len(sys.argv) == 1:
        print("0")
        exit()
    total = 0
    while i < len(sys.argv):
        total = total + int(sys.argv[i])
        i += 1
    print(total)
