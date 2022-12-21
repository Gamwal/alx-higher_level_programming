#!/usr/bin/python3
"""Defines a Square Class object"""


class Square:
    """Create a class Square."""
    def __init__(self, size=0):
        """Initializes the class object.

        Args:
            size (:obj: int, optional): The size of the square
                must be >= 0.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the current sqaure area."""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves the size attribute of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Changes the size attribute of the square object"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
