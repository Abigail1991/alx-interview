#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    """Checks if data is valid UTF8
    Arguments:
        data: list if integers
    Return:
        True if data is valid UTF8, False if not
    """

    expected_bytes = 0
    
    for num in data:
        # If no expected bytes, this is a new character
        if expected_bytes == 0:
            if (num >> 7) == 0:
                continue
            elif (num >> 5) == 0b110:
                expected_bytes = 1
            elif (num >> 4) == 0b1110:
                expected_bytes = 2
            elif (num >> 3) == 0b11110:
                expected_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte
            if not is_start_byte(num):
                return False
            expected_bytes -= 1
        
    # All bytes have been checked, if there are still expected bytes, it's invalid
    return expected_bytes == 0
