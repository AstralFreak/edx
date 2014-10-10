"""Coordinates of a point in a two-dimensional space (<x,y>)"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

class Coordinate(object):
    '''
    Coordinates of a point in a two-dimensional space (<x,y>)
    '''
    def __init__(self,x,y):
        '''
        Create the coordinate <x,y>
        :param x: X-coordinate
        :param y: Y-coordinate
        :return: Coordinate <x,y>
        '''
        self.x = x
        self.y = y

    def getX(self):
        '''
        Return the x-coordinate of the point
        :return: X-coordinate
        '''
        return self.x

    def getY(self):
        '''
        Return the y-coordinate of the point
        :return: Y-coordinate
        '''
        return self.y

    def __str__(self):
        '''
        Return the string representation of the coordinates
        :return: <x,y>
        '''
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        '''
        Check if two coordinates are equal (i.e. correspond to the same point)
        :param other: Coordinate
        :return: Coordinates refer to the same point
        '''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''
        Return the constructor call to obtain the coordinates for the same point
        :return: Coordinate(<X>,<Y>)
        '''
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ")"