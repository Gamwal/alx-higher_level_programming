#!/usr/bin/python3
"""Rectangle module that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Init method for the BaseGeometry class"""
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """Implemented area method of the rectangle class object"""
        return self.__width * self.__height

    def __str__(self):
        """string magic method"""
        return "Rectangle {}/{}".format(self.__width, self.__height)
