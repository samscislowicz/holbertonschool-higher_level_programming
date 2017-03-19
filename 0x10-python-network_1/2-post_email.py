#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode(encoding='UTF-8'))
