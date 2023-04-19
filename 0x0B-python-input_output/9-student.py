#!/usr/bin/python3
"""
Student class that defines student by
    first_name
    last_name
    age
"""


class Student:
    """
    Student class object
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __dict__(self):
        return dict({'first_name': self.first_name,
                     'last_name': self.last_name,
                     'age': self.age})
    
    def to_json(self):
        """Public method to retrieve a dict representation of object"""
        return self.__dict__
