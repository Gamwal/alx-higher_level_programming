#!/usr/bin/python3
""" Time for an interview! """


if __name__ == '__main__':
    import requests
    import sys
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    resp = r.json()
    for i in range(10):
        try:
            print("{}: {}".format(
                resp[i].get("sha"),
                resp[i].get("commit").get("author").get("name")))
        except IndexError:
            pass
