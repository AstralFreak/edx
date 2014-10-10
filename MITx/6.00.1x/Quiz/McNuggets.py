'''Find if there's a combination <a, b, c> such that 6*a + 9*b + 20*c = n'''

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def McNuggets(n):
    '''
    Find if there's a combination <a, b, c> such that 6*a + 9*b + 20*c = n
    :param n: Number of items
    :return: True if and only if a combination <a, b, c> exists
    '''
    if n % 6 == 0 or n % 9 == 0 or n % 20 == 0:
        return True
    coefficient = {'a': 0, 'b': 0, 'c': 0}
    solution = False
    while coefficient['c']*20 <= n:
        while coefficient['c']*20 + coefficient['b']*9 <= n:
            while coefficient['c']*20 + coefficient['b']*9 + coefficient['a']*6 < n:
                coefficient['a'] += 1
            if coefficient['c']*20 + coefficient['b']*9 + coefficient['a']*6 == n:
                return True
            coefficient['a'] = 0
            coefficient['b'] += 1
        coefficient['b'] = 0
        coefficient['c'] += 1
    return False