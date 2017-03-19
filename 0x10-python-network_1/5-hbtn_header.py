#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":

    url = sys.argv[1]
    r = requests.get(url)
    html = r.headers
    print(html['X-Request-Id'])
