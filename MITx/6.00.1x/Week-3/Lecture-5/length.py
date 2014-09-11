"""Calculate the length of a string"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def lenIter(aStr):
    '''
    Calculate iteratively the length of a string
    :param aStr: String
    :return: Length of the string
    '''
    assert type(aStr) == str
    length = 0
    for char in aStr:
        length += 1
    return length

def lenRecur(aStr):
    '''
    Calculate recursively the length of a string
    :param aStr: String
    :return: Length of the string
    '''
    assert type(aStr) == str
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])