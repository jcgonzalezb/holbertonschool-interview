#!/usr/bin/python3
"""
This project module contains one method that determines if a
given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    This is a method that determines if a given data set
    represents a valid UTF-8 encoding.
    :type data: List[int]
    :rtype: bool
        Returns: True if data is a valid UTF-8 encoding,
        else return False.
    """
    try:
        bytes(data).decode()
    except Exception:
        return False
    return True
