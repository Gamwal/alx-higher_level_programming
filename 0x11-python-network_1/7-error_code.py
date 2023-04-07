#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
    to the URL and displays the body of the response."""


if __name__ == '__main__':
    import requests
    import sys
    r = requests.get(sys.argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
