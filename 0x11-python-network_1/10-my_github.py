#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = 'https://api.github.com/user'
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=basic)
    print(r.json())
