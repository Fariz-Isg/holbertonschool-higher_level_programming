#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class with basic attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Args:
            attrs (list): Optional list of attribute names to retrieve

        Returns:
            dict: Dictionary containing requested or all instance attributes
        """
        if attrs is None:
            return self.__dict__
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict
