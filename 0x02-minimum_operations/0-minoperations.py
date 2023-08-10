#!/usr/bin/python3
"""Minimum Operations module.

This module contains a function that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): the number of characters to reach.

    Returns:
        int: the fewest number of operations needed, 0 otherwise.

    """
    char = n
    operations = 0
    divisor = 2

    while char > 1:
        if char % div == 0:
            operations += div
            char /= div
        else:
            div += 1

    return operations
