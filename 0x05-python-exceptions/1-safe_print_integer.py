#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = value/1
        print("{:d}".format(value))
        return True
    except Exception:
        return False
