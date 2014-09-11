"""Calculate the Greatest Common Divisor of two numbers"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def gcdIter(a, b):
    '''
    Calculate iteratively the Greatest Common Divisor of two numbers
    :param a: First number
    :param b: Second number
    :return: GCD(a, b)
    '''
    divisor = min(a, b)
    while divisor > 1 and (a % divisor != 0 or b % divisor != 0):
        divisor -= 1
    return divisor

def gcdRecur(a, b):
    '''
    Calculate recursively the Greatest Common Divisor of two numbers
    :param a: First number
    :param b: Second number
    :return: GCD(a, b)
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)