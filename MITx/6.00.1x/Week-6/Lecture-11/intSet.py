'''Set of integers'''

__author__ = 'Nicola Moretto'
__license__ = "MIT"

class intSet(object):
    '''
    Set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once.
    '''
    def __init__(self):
        '''
        Create an empty set of integers
        '''
        self.vals = []

    def insert(self, e):
        '''
        Assumes e is an integer and inserts e into self
        :param e: Integer
        '''
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        '''
        Assumes e is an integer and returns True if and only if is in set
        :param e:
        :return: If e is in the set
        '''
        return e in self.vals

    def remove(self, e):
        '''
        Assumes e is an integer and removes e from self.
        Raises ValueError if e is not in self
        :param e:
        '''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        '''
        Returns a string representation of the integer set
        :return: String representation of the integer set
        '''
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        '''
        Return the intersection of two integer sets (a list of the distinct values in both sets)
        :param other: intSet
        :return: Intersection of integer sets (without duplicates)
        '''
        intersection = intSet()
        for value in self.vals:
            if other.member(value):
                intersection.insert(value)
        return intersection

    def __len__(self):
        '''
        Return the number of integers in the set
        :return: Number of integers in the set
        '''
        return len(self.vals)