#!/usr/bin/python3
"""
This project module contains one method that determines if a
given data set represents a valid UTF-8 encoding.
"""

NUMBER_OF_BITS_PER_BLOCK = 8
MAX_NUMBER_OF_ONES = 4


def validUTF8(data):
    """
    This is a method that determines if a given data set
    represents a valid UTF-8 encoding.
    :type data: List[int]
    :rtype: bool
        Returns: True if data is a valid UTF-8 encoding,
        else return False.
    """
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
        if number == 0:  # single byte char
            index += 1
            continue

        # validate multi-byte char
        number_of_ones = 0
        while True:  # get the number of significant ones
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (NUMBER_OF_BITS_PER_BLOCK - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break

            if number_of_ones > MAX_NUMBER_OF_ONES:
                return False  # too much ones per char sequence

        if number_of_ones == 1:
            return False  # there has to be at least 2 ones

        # move on to check the next byte in a multi-byte char sequence
        index += 1

        # check for out of bounds and exit early
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False

        # every next byte has to start with "10"
        for i in range(index, index + number_of_ones - 1):
            number = data[i]

            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 1:
                return False
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 0:
                return False

            index += 1

    return True
