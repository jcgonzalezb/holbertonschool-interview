#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins: list, total: int) -> int:
    if total <= 0:
        return 0
    total_list = sum(coins)
    if total_list > total:
        return -1
    new_coins = []
    sorted_coins = coins.sort()
    highest_value_coin = sorted_coins[-1]
    if 2 * highest_value_coin > total:
        new_coins.append(highest_value_coin)
        sorted_coins.pop()
