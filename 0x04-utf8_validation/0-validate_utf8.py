#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    """Checks if data is valid UTF8
    Arguments:
        data: list if integers
    Return:
        True if data is valid UTF8, False if not
    """

    nByte = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7

        if nByte == 0:
            while byte & mask:
                nByte += 1
                mask = mask >> 1

            if nByte == 0:
                continue

            if nByte == 1 or nByte > 4:
                return False

        else:
            if not (byte & mask1) and (byte & mask2):
                return False
        nByte -= 1

    return nByte == 0
