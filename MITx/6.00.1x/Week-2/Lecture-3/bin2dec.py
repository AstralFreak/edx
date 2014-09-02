"""Convert positive binary integers to decimal"""
import re

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def bin2dec(x):
    """Convert a positive binary integer to decimal
    :param x: Positive binary integer
    :return: Decimal number
    """
    if re.match("^[0-1]+$", str(x)):
        # <x> is a valid binary integer
        value = x
        result = 0
        power = 0
        for digit in x:
            result = int(digit) + result*2
        if x[0] == '-':
            value = -value
        return result
    else:
        # <x> is NOT a valid binary integer
        return None
