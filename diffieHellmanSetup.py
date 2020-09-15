from random import randrange, getrandbits
from Crypto.Util import number
from math import gcd

from math import sqrt

def isPrime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def power( x, y, p):

    res = 1
    x = x % p

    while (y > 0):

        if (y & 1):
            res = (res * x) % p

        y = y >> 1 # y = y/2
        x = (x * x) % p

    return res

def findPrimefactors(s, n) :
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :
            s.add(i)
            n = n // i
    if (n > 2) :
        s.add(n)


def findPrimitive( n) :
    s = set()

    if (isPrime(n) == False):
        return -1

    phi = n - 1

    findPrimefactors(s, phi)

    for r in range(2, phi + 1):

        flag = False
        for it in s:

            if (power(r, phi // it, n) == 1):

                flag = True
                break

        if (flag == False):
            return r
    return -1

# Driver Code

p = number.getPrime(5)
n = findPrimitive(p)
