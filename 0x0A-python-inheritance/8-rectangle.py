#!/usr/bin/python3
"""Geometry Module with area method"""


class BaseGeometry:
    """Empty base class with an area method"""

    def __init__(self, width, height):
        self.width = width
        self.height = self.integer_validator("height", height)

    def area(self):
        """area method that does nothing yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validated value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
