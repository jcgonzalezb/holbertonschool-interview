#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


from django.urls import reverse


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
    coins.sort(reverse=True)
    while total > 0 and len(coins) > 0:
        div = total // coins[0]
        total = total % coins[0]
        new_coins.append(div)
        coins.pop(0)
    if len(coins) == 0 and total != 0:
        return -1
    return sum(new_coins)
