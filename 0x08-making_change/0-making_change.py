#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


from math import remainder


def makeChange(coins: list, total: int) -> int:
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
