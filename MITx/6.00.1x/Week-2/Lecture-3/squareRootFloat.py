"""Calculate the square cube of a float number"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def squareRootFloat(x, step, precision):
    '''
    Calculate the square root of a float number through exhaustive enumeration with given step and precision
    :param x: Float number
    :param step: Enumeration step
    :param precision: Square root precision
    :return: Square root of the float number
    '''
    if x < 0 or step <= 0 or precision <= 0:
        return None

    # x>=0
    value = 0
    while abs(value**2-x) > precision and value**2 < x:
        value += step

    if abs(value**2-x) <= precision:
        return value
    else:
        return None