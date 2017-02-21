# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:06:24 2015

@author: Joe Vandagriff
"""

from numtheory import isPrime
from totient import primes
from collections import defaultdict

def sum_digits(n):
    r = 0
    while n:
        r,n = r+ n%10, n/10
    return r
s = 0
#prime_lookup = defaultdict(bool)

xList = [1,2,4,6,8]
iterCount = 0
while iterCount < 12:
    newList = []
    for n in xList:
        for i in range(10):
            x = n*10+i
            if x%sum_digits(x) == 0: newList.append(x)
    for n in newList:
        for i in [1,3,7,9]:
            x = n*10+i
            if int(str(n)[0]) != 1 and isPrime(n/sum_digits(n)) and isPrime(x):
                s+=x
                print x
        
    xList = newList[:]
    iterCount+=1
        