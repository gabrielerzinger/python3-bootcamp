# Making a speed test decorator
from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print("Time Elapsed: {}".format(t2-t1))
        return result
    return wrapper


'''Generates all primes thro n'''
@speed_test
def genprime(n):
    primes = [0 for i in range(n+2)]
    for i in range(1, n+1):
        td = 0
        for j in range(1, i+1):
            if i % j == 0:
                td = td + 1
        if td <= 2:
            primes[i] = 1

'''Generates all primes thro n using sieve'''
@speed_test
def sieve(n):
    primes, primes[2], p = [0 if i % 2 == 0 else 1 for i in range(n+2)], 1, 3
    while p*p <= n:
        if primes[p]:
            for i in range(p*2, n+1, p):
                primes[i] = 0
        p = p + 2


genprime(10000)
sieve(100000)
