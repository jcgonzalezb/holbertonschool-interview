#!/usr/bin/python3
"""
This project module contains one method that returns a list
of lists of integers representing the Pascal’s triangle of n.
"""
from math import log, ceil

def minOperations(n):
    """
    This is a method that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n == 0 or n == 1:
        return 0
    
    if n == 2:
        return 2
    
    flag = False
    if n > 2:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
            return n
        return ceil(log(n, 2))
