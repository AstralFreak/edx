"""Prime number generator"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def genPrimes():
    '''
    Generate prime numbers, one at the time
    Use the next() method to get the next prime number
    :return: Increasing sequence of prime numbers
    '''
    primes = []
    number = 2
    isPrime = True
    while True:
        for prime in primes:
            if number % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(number)
            yield number
        number += 1
        isPrime = True