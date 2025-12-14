#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """Class that defines base geometry"""

    def area(self):
        """Calculate the area

        Raises:
            Exception: Always, with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
