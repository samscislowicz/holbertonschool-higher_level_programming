#!/usr/bin/python3
"""

"""
import requests
import sys

if __name__ == "__main__":
    search = sys.argv[1]
    url = "https://swapi.co/api/people/?search=" + search
    r = requests.get(url)
    response = dict(r.json())
    print("Number of result: {}".format(response.get(count)))
    for name in response.get("results"):
        print(response.get("name"))
