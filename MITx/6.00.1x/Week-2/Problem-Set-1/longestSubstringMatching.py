"""Find the longest substring in alphabetical order occurring in a string"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def longestSubstringMatching(pattern, string):
    '''
    Return the longest substring in alphabetical order occurring in a string
    :param pattern: Pattern
    :param string: String
    :return: Long substring in alphabetical order
    '''
    startIndex = 0
    stringLength = len(string)
    substring = ""
    substringLength = 0

    while startIndex < stringLength-substringLength:
        currentIndex = startIndex
        nextIndex = startIndex + 1
        while nextIndex<stringLength and string[currentIndex]<=string[nextIndex]:
            currentIndex = nextIndex
            nextIndex += 1
        if len(substring)<nextIndex-startIndex:
            substring = string[startIndex:nextIndex]
            substringLength = len(substring)
        startIndex += nextIndex-startIndex

    return substring