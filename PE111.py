# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:33:13 2016

@author: Joe Vandagriff
"""

from numtheory import isPrime
from itertools import combinations

def nines(d):
    primes = []
    for exp in range(10):
        
        powers = [x for x in range(10)]
        powers.remove(exp)
        base_digits = sum([d*10**i for i in powers])
        for i in range(10):
            if exp == 9 and i == 0: continue
            candidate = base_digits + i*10**exp
            if isPrime(candidate):
                primes.append(candidate)
    return primes

def eights(d):
    primes = []
    replacement_exponents = [x for x in combinations(range(10),2)]
    for (a,b) in replacement_exponents:
        powers = [x for x in range(10)]
        powers.remove(a)
        powers.remove(b)
        
        base_digits = sum([d*10**i for i in powers])
        
        for i in range(10):
            for j in range(10):
                if b == 9 and j == 0: continue
                candidate = base_digits + i*10**a + j*10**b
                if isPrime(candidate):
                    primes.append(candidate)
    return primes

s = 0

for i in range(1,10):
    for j in [1,3,7,9]:
        candidate = i*10**9 + j
        if isPrime(candidate):
            s+=candidate

for d in range(1,10):
    nine_list = nines(d)
    print nine_list
    s += sum(nine_list)
    if len(nine_list) == 0:
        s+= sum(eights(d))
print s