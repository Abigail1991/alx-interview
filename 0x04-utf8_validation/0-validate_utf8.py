#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    """Checks if data is valid UTF8
    Arguments:
        data: list if integers
    Return:
        True if data is valid UTF8, False if not
    """

    nbBytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7

        if nbBytes == 0:
            while byte & mask:
                nbBytes += 1
                mask = mask >> 1

            if nbBytes == 0:
                continue

            if nbBytes == 1 or nbBytes > 4:
                return False

        else:
            if not byte & mask1 and byte & mask2:
                return False
        nbBytes -= 1

    return nbBytes == 0
