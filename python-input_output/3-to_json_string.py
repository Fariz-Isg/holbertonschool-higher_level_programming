#!/usr/bin/python3
"""Module that defines a to_json_string function"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)

    Args:
        my_obj: The object to serialize to JSON

    Returns:
        str: JSON string representation of the object
    """
    return json.dumps(my_obj)
