#!/usr/bin/python3
"""The first Base class object"""


class Base:
    """The first Base class object"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The initialization of the class object

        Args:
            id (int): the id of the class object

        Returns:
            Base class instance with id, id

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
