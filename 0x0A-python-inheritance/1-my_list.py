#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """list object inheriting from python list."""

    def print_sorted(self):
        """method to print sorted list."""
        print(sorted(self))
