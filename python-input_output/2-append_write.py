#!/usr/bin/python3
"""Module that defines an append_write function"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8) and return count

    Args:
        filename (str): The name of the file to append to (default: "")
        text (str): The text to append to the file (default: "")

    Returns:
        int: The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
