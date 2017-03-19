#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
        html = response.read()
print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {:s}""".format(type(html), html,
                                 html.decode(encoding='UTF-8')))
