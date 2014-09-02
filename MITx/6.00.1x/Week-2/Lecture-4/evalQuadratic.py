"""Calculate the value of the quadratic ax^2 + bx + c"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def evalQuadratic(a, b, c, x):
    '''
    Calculate the value of the quadratic ax^2 + bx + c
    :param a: Coefficient of second grade
    :param b: Coefficient of first grade
    :param c: Constant
    :param x: Variable
    :return: Quadratic value
    '''
    return a * x**2 + b * x + c
