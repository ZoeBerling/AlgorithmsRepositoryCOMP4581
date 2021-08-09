import random
from math import sqrt
from time import time
import pandas as pd
"""Zoe Berling Algorithms Lab 3 RSA Cracking"""
"""Estimate time: how long it takes to crack RSA encryption keys"""


def isPrime(p):
    """Takes in a number, p and return true if it is prime and false otherwise"""
    # divide p by all numbers between 2 and p (or sqrt(p))
    n = False
    if p > 1:
        if p == 2 or p == 3:
            return True
        else:
            for i in range(2, int(sqrt(p))+1):
                if (p % i) == 0:
                    n = False
                    break
                else:
                    n = True
    else:
        return False
    return n


def nBitPtime(n):
    """generate a random prime number that is n bits long( n-bit can range from 0... 2^n)"""
    rand = random.random()
    num = int(rand * 2**n)
    if isPrime(num) == True:
        return num
    else:
        num = nBitPtime(n)
    return num


def factor(pq):
    """factor PQ by dividing by every number between 2 and PQ to find the one that evenly divides it"""
    p, q = 0, 0
    for i in range(2, pq):
        if pq % i == 0:
            p = i
            q = pq / p
            break
    return p, q


timinglist = []
for b in range(15, 20): # Evaluated # of bits incrementally
    pq = nBitPtime(b) * nBitPtime(b)
    t1 = time()
    b20 = factor(pq)
    t2 = time()
    timing = round((t2 - t1)*1000, 3)
    timinglist.append([b, timing])
df = pd.DataFrame(timinglist, columns=("b","timing (ms)"))
print(df)
# with open("lab3test.csv", 'a') as f:
    # df.to_csv(f, mode='a', header=f.tell()==0)

"""To crack a 2 x 1025-bit prime key with this program on my laptop
 it would take approximately 1.9E+304 milliseconds, which is about 6.02E+293 years."""
