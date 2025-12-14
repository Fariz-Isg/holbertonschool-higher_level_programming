#!/usr/bin/python3
"""Module that defines a read_file function"""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout

    Args:
        filename (str): The name of the file to read (default: "")
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
