#!/usr/bin/python3
import requests
if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    ok = r.text
    print('Body response:')
    print('    - type: {}'.format(type(ok)))
    print('    - content: {}'.format(ok))
