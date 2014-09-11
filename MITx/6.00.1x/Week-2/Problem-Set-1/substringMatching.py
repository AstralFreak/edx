"""Find the number of occurrences of a pattern in a string"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def substringMatching(pattern, string):
    '''
    Return the number of occurrences of a pattern in a string"
    :param pattern: String pattern
    :param string: String
    :return: Number of occurrences of <pattern> in <string>
    '''
    startIndex = 0
    occurrences = 0
    stringLength = len(string)
    patternLength = len(pattern)

    while startIndex <= stringLength-patternLength:
        if string[startIndex:startIndex+patternLength] == pattern:
            occurrences += 1
        startIndex += 1

    return occurrences