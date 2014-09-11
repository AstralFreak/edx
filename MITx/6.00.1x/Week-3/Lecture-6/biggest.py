"""Find the longest list contained in a dictionary"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def biggest(aDict):
    '''
    Return the key of the longest list contained in a dictionary
    :param aDict: Dictionary of lists
    :return: Key of the longest list
    '''
    biggestKey = None
    biggestLength = -1
    for key in aDict:
        if len(aDict[key]) > biggestLength:
            biggestKey = key
            biggestLength = len(aDict[key])
    return biggestKey

