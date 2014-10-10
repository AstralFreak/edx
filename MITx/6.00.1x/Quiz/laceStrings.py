'''Return a string obtained interlacing two input strings'''

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def laceStrings(s1, s2):
    '''
    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    :param s1: string
    :param s2: string
    :return: Interlaced strings
    '''
    commonLength = min(len(s1), len(s2))
    totalLength = len(s1) + len(s2)
    lacedString = ''
    if totalLength > 0:
        for step in range(0, commonLength):
            lacedString += s1[step] + s2[step]
        if len(s1) > len(s2):
            lacedString += s1[commonLength:len(s1)]
        elif len(s2) > len(s1):
            lacedString += s2[commonLength:len(s2)]
    return lacedString