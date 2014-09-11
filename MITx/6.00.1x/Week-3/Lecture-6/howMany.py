"""Calculate the total number of elements contained in a dictionary of lists"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def howMany(aDict):
    '''
    Calculate the total number of elements contained in a dictionary of lists
    :param aDict: Dictionary of lists
    :return: Total size of lists
    '''
    count = 0
    for key in aDict:
        count += len(aDict[key])
    return count