#!/usr/bin/python3
"""Define a class named Square"""


class Square:
    """Defines a Square by size"""
    def __init__(self, size):
        """
        initializes Square object.

        Args:
            size (int): Size of the Square object.
        """
        self.__size = size
