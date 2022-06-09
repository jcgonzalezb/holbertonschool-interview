#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Function that  determine the fewest number of coins needed to meet
    a given amount total.
        Returns:
            Fewest number of coins needed to meet total.
            If total is 0 or less, return 0.
            If total cannot be met by any number of coins you have, return -1.

    """
    if total < 0:
        return 0

    new_coins = []
    coins.sort()
    while total > 0 and len(coins) > 0:
        div = total // coins[-1]
        total = total % coins[-1]
        new_coins.append(div)
        coins.pop()
        if len(coins) == 0 and total != 0:
            return -1
    return sum(new_coins)
