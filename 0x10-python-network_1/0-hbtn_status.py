#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    """
    This module is a Python script that fetches https://intranet.hbtn.io/status
    """
with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
    html = response.read()
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(html), html,
                                 html.decode(encoding='UTF-8')))
