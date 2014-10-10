'''Find an approximate value of the fixed point of a function'''

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def fixedPoint(f, epsilon):
    '''
    Return the best guess of the fixed point of a function f()
    being less-than-epsilon away from f(guess) after at most 100 trials
    :param f: function of one argument that returns a float
    :param epsilon: float precision
    :return: Best approximated guest (i.e. |guess-f(guess)|<epsilon)
    '''
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)