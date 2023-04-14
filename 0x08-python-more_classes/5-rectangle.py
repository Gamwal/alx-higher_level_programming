#!/usr/bin/python3
""" This is the definition of a class object Rectangle"""


class Rectangle:
    """Simple Rectangle Class"""
    def __init__(self, width=0, height=0):
        """init method of the Rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area function of the Rectangle object"""
        if (self.height == 0) or (self.width == 0):
            return 0
        else:
            return self.width * self.height

    def perimeter(self):
        """area function of the Rectangle object"""
        if (self.height == 0) or (self.width == 0):
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """String representation of the Rectangle object"""
        if (self.height == 0) or (self.width == 0):
            return ""
        else:
            empty_str = ""
            for i in range(self.height):
                for j in range(self.width):
                    empty_str += "#"
                if i != (self.height) - 1:
                    empty_str += "\n"
            return empty_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
