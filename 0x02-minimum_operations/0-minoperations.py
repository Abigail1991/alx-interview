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
    chars = n
    operations = 0
    div = 2

    while chars > 1:
        if chars % div == 0:
            operations += div
            chars /= div
        else:
            div += 1

    return operations
