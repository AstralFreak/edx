"""Calculate the given function on each element of a list"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def applyToEach(L, f):
    '''
    Calculate the given function on each element of a list
    :param L: List of values
    :param f: Function
    :return: L -> f(L)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, 9]

#  L6 Problem 7a
applyToEach(testList, abs)

#  L6 Problem 7b
def increment(x):
    return x+1
applyToEach(testList, increment)

#  L6 Problem 7c
def square(x):
    return x**2
applyToEach(testList, square)