#!/usr/bin/python3
def count(n):
    if len(n) == 0:
        print("0 arguments.")
    elif len(n) == 1:
        print("1 argument:")
        print("1: {}".format(n[0]))
    else:
        print("{} arguments:".format(len(n)))
        for i, j in enumerate(n):
            p = i + 1
            print("{}: {} ".format(p, j))


if __name__ == "__main__":
    import sys
    count(sys.argv[1:])
