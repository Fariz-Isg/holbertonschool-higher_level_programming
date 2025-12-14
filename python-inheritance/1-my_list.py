#!/usr/bin/python3
"""Module that defines a MyList class"""


class MyList(list):
    """A list subclass with additional methods"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
