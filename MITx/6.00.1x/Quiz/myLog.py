'''Calculate the best lower integer approximation of log_b(x)'''

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def myLog(x, b):
    '''
    Calculate the best lower integer approximation of log_b(x)
    :param x: a positive integer
    :param b: a positive integer (>= 2)
    :return: best lower integer approximation of log_b(x)
    '''
    value = 0
    while b**value < x:
        value += 1
    if b**value == x:
        return value
    else:
        return value-1