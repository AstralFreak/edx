"""Calculate the exponential of a base"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def iterPower(base, exp):
    '''
    Calculate iteratively the exponential of a base
    :param base: Base
    :param exp: Exponent
    :return: Exponential of the base
    '''
    result = 1
    while(exp > 0):
        result *= base
        exp -= 1
    return result

def recurPower(base, exp):
    '''
    Calculate recursively the exponential of a base
    :param base: Base
    :param exp: Exponent
    :return: Exponential of the base
    '''
    if exp == 0:
        return 1
    return base*recurPower(base, exp-1)

def recurPowerNew(base, exp):
    '''
    Calculate recursively the exponential of a base
    :param base: Base
    :param exp: Exponent
    :return: Exponential of the base
    '''
    if exp == 0:
        return 1
    if exp % 2 ==0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base*recurPowerNew(base, exp-1)