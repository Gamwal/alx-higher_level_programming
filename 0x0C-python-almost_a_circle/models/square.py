#!/usr/bin/python3
"""Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance of a Square object.

        Args:
            size (int): The size of the square.
            x (int): x-coord of the square.
            y (int): y-coord of the square.
            id (int): instance id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <size>
        """
        save = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        save += f"{self.size}"
        return save

    @property
    def size(self):
        """set/get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
