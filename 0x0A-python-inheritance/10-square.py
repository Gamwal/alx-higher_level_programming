#!/usr/bin/python3
"""Square module that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square object that inherits from Rectangle"""
    def __init__(self, size):
        """initmethod of the Square object that takes in size"""
        self.__size = super(Rectangle, self).integer_validator("size", size)

    def area(self):
        """Area method of the Square object"""
        return self.__size * self.__size
