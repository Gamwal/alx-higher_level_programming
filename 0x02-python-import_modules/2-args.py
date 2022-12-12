#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = sys.argv[1:]
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
