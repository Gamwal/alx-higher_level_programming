#!/usr/bin/python3
"""Square module that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square object that inherits from Rectangle"""
    def __init__(self, size):
        """initmethod of the Square object that takes in size"""
        self.__size = Rectangle.BaseGeometry.integer_validator(self,
                                                               "size", size)
