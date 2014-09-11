"""Test recursively with the bisection method if a sorted string contains a given character"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def isIn(char, aStr):
    '''
    Check if a string contains a given character
    :param char: Single character
    :param aStr: Sorted string
    :return: If the string contains the character
    '''
    assert type(aStr) == str and type(char) == str
    if len(aStr) <= 1:
        return aStr == char
    else:
        middle = (len(aStr)-1)/2
        if aStr[middle] == char:
            return True
        elif aStr[middle] < char:
            return isIn(char, aStr[middle+1:])
        else:
            return isIn(char, aStr[:middle])