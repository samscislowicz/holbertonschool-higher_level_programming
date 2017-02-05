#!/usr/bin/python3
import sys
"""
Module input and output
"""

total = 0
stat_code = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        total += int(line.split()[-1])
        stat_code[line.split()[-2]] += 1
        if (sum(stat_code.values()) % 10 == 0):
            print("File size:{}".format(total))
            for key, value in sorted(stat_code.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    print("File size:{}".format(total))
    for key, value in sorted(stat_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))
