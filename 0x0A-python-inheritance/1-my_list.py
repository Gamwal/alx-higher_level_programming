#!/usr/bin/python3


class MyList(list):
    """list object inheriting from python list."""

    def __init__(self):
        """initializes the object"""

        list.__init__(self)

    def print_sorted(self):
        """method to print sorted list."""

        print(sorted(self))
