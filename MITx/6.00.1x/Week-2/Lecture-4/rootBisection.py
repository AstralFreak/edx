"""Find the nth root of a number with the bisection method."""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def rootBisection(x, power, precision):
    '''
    Find the nth root of a number with the bisection method.
    :param x: Number
    :param power: Root
    :param precision: Precision
    :return: power-th root of x
    '''
    if power < 1 or precision < 0:
        return None
    if power == 1:
        return x
    if x < 0 and power%2 == 0:
        return None

    low = min(-1, x)
    high = max(1, x)
    value = (low+high)/2.0
    while abs(value**power-x) > precision:
        if value**power < x:
            low = value
        else:
            high = value
        value = (low+high)/2.0

    return value