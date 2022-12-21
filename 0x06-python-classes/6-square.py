#!/usr/bin/python3
"""Defines a Square Class object"""


class Square:
    """Create a class Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class object.

        Args:
            size (:obj: int, optional): The size of the square
                must be >= 0.

            position (:obj: tuple, optional): The position of the
                square.

        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints the square to the stdout"""

        if self.__size == 0:
            print("")
            return
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")

    @property
    def position(self):
        """retrieves the values of the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute value."""

        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(num, int) for num in value) or\
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
