"""Convert decimal numbers - integer or fractional - to binary"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def dec2bin(x):
    """
    Convert a decimal number - integer or fractional inside the interval [-1, 1]  - to binary
    :param x: Decimal number (integer or fractional inside the interval [-1, 1])
    :return: Binary number
    """
    # If x is a float number outside the interval [-1, 1], STOP
    value = abs(x)
    if type(x) != type(1) and value > 1:
        return None

    result = ''
    if value == 0:
        return '0'
    elif value < 1:
        # Fractional number inside the interval [-1, 1]
        power = 0
        while value*(2**power)%1 != 0:
            power += 1
        value = int(value*(2**power))

    # Convert <value> in binary and save to <result>
    while value > 0:
        result = str(value%2) + result
        value = value/2

    # If <x> is negative, prefix the '-' (minus) sign
    if x < 0:
        result = '-' + result

    # If <x> is a fractional number inside the interval [-1, 1], right shift of p-len(result) position
    if abs(x) < 1:
        for i in range(power - len(result)):
            result = '0' + result
        result = result[0:-power] + '.' + result[-power:]

    return result