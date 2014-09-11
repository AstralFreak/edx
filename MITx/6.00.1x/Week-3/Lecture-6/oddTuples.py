"""Remove all elements whose index is odd from the given tuple"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def oddTuples(aTup):
    '''
    Remove all elements whose index is odd from the given tuple
    :param aTup: Tuple
    :return: A new tuple with ALL and ONLY the elements whose index is even
    '''
    rTup = ()
    i = 0
    while i < len(aTup):
        if i%2==0:
            rTup = rTup + (aTup[i],)
        i += 1
    return rTup