#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) != int:
        a = int(a)
    if type(b) != int:
        b = int(b)
    return a + b

if __name__ == "__main__":
    add_integer(a, b=98)
