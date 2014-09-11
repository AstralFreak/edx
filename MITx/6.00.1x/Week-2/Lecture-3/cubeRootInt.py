"""Calculate the root cube of an integer"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def cubeRootInt(x):
    '''
    Calculate the root cube of an integer
    :param x: Integer
    :return: Root cube of the integer
    '''
    answer = 0
    value = abs(x)

    while answer**3 < value:
        answer += 1

    # answer**3 >= value
    if answer**3 != value:
        return None
    else:
        if x<0:
            answer *= -1
        return  answer