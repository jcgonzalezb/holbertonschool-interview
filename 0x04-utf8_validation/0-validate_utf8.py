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
    successive_10 = 0
    for b in data:
        b = bin(b).replace('0b', '').rjust(8, '0')
        if successive_10 != 0:
            successive_10 -= 1
            if not b.startswith('10'):
                return False
        elif b[0] == '1':
            successive_10 = len(b.split('0')[0]) - 1
    return True
