"""Count the number of vowels contained in the given string"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def countVowels(string):
    '''
    Count the number of vowels contained in the given string
    :param string: Alphabetic string
    :return: Number of vowels
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    numVowels = 0
    for char in string:
        if char in vowels:
            numVowels += 1
    return numVowels