#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        print("No result")
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        print("No result")
    elif len(sys.argv) < 2:
            letter = ""
    else:
        letter = sys.argv[1]
        payload = {'q': letter}
        r = requests.post(url, data=payload)
        try:
            response = r.json()
            if response.get("id") is None:
                print("No result")
            else:
                print("[{}] {}".format(response.get("id"),
                                       response.get("name")))
        except:
            print("Not a valid JSON")
