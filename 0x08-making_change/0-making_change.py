#!/usr/bin/python3
""" Making Change module """


def makeChange(coins, total):
    """ makeChange: finds lowest number of coins for a given sum """
    if total <= 0:
        return 0
    change = 0
    num_coins = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)
    while(change < total and index < len(coins)):
        if (change + sorted_coins[index] <= total):
            change += sorted_coins[index]
            num_coins += 1
        else:
            index += 1
    if change == total:
        return num_coins
    return -1
