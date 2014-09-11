"""Check if a given character is a vowel."""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def isVowel(char):
    '''
    Check if a given character is a vowel.
    :param char: Alphabetic character
    :return: True if the character is a vowel (False otherwise)
    '''
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
        return True
    else:
        return False

def isVowelAlt(char):
    '''
    Check if a given character is a vowel (alternative version).
    :param char: Alphabetic character
    :return: True if the character is a vowel (False otherwise)
    '''
    letters = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if char in letters:
        return True
    else:
        return False