#!/usr/bin/python3
""" 
You have n number of locked boxes. Each box is numbered 
sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    This is a method that determines if all the
    boxes can be opened.
    Returns:
        True if all boxes can be opened, else return False.
    """

    unlocked = []
    keys = []
    for i in boxes:
        unlocked.append(0)
    if len(boxes) > 0:
        unlocked[0] = 1
        keys.append(0)
    while keys:
        key = keys.pop(0)
        new_keys = boxes[key]
        unlocked[key] = 1
        for new_key in new_keys:
            if new_key < len(unlocked) and unlocked[new_key] == 0:
                keys.append(new_key)
    for unlock in unlocked:
        if unlock != 1:
            return False
    return True
