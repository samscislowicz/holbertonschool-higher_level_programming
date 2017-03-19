#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
        html = response.read()
print("Body response:")
print("    - type: <class 'bytes'>")
print("    - content: {}".format(html))
print("    - utf8 content: OK")
