#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""
def makeChange(coins, total):
    for i in coins:
        total_list += coins[i]
    return total_list

