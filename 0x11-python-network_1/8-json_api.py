#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == '__main__':
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    sys_len = len(sys.argv)
    if sys_len < 2 or sys.argv[1].isalpha() is not True:
        payload = {'q': ""}
    else:
        payload = {'q': sys.argv[1]}
    r = requests.post(url, data=payload)
    try:
        json = r.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print("Not a valid JSON")
