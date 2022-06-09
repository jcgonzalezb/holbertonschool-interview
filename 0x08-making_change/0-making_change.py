#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


from math import remainder


def makeChange(coins: list, total: int) -> int:
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
    total_list = sum(coins)
    if total_list > total:
        return -1
    new_coins = []
    sorted_coins = sorted(coins)
    remainder = total
    while remainder > 0:
        rem = remainder % sorted_coins[-1]
        div = remainder // sorted_coins[-1]
        new_coins.append(div)
        remainder = rem
        sorted_coins.pop()
    return int(sum(new_coins))
