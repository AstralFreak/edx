"""Problem 5 | Lecture 4: takes in three numbers and returns a value based on the value of x."""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x
    :param lo: Minimum value
    :param x: Current value
    :param hi: Maximum value
    :return: x <= x in [lo, hi], lo <= x < lo, hi <= x > hi
    '''
    return min(max(x, lo), hi)