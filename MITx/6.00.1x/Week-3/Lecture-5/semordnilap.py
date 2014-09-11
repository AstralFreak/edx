"""Verify if two strings are a semordnilap (i.e. the first string can be obtained reversing the second (and vice versa)"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def isSemordnilap(str1, str2):
    '''
    Verify if two strings are a semordnilap
    :param str1: First string
    :param str2: Second string
    :return: True if the two strings are a semordnilap
    '''
    def semordnilapWrapper(str1, str2):
        '''
        Perform an input validation before checking if the strings are a semordnilap
        :param str1: First string
        :param str2: Second string
        :return: True if the two strings are a semordnilap
        '''
        # A single-length string cannot be semordnilap
        if len(str1) == 1 or len(str2) == 1:
            return False
        # Equal strings cannot be semordnilap
        if str1 == str2:
            return False
        return semordnilap(str1, str2)

    def semordnilap(str1, str2):
        '''
        Check if the two strings are a semordnilap
        :param str1: First string
        :param str2: Second string
        :return: True if the two strings are a semordnilap
        '''
        if len(str1) != len(str2):
            return False
        if len(str1) == 1: # len(str2) == 1
            if str1 == str2:
                return True
            else:
                return False
        else:
            if str1[0] == str2[-1]:
                return semordnilap(str1[1:], str2[:-1])
            else:
                return False

    return semordnilapWrapper(str1, str2)