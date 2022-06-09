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
    if total <= 0:
        return 0
    new_coins = []
    sorted_coins = sorted(coins)
    while total > 0 and len(sorted_coins) > 0:
        div = total // sorted_coins[-1]
        total = total % sorted_coins[-1]
        new_coins.append(div)
        sorted_coins.pop()
        if len(sorted_coins) == 0 and total != 0:
            return -1
    return sum(new_coins)
