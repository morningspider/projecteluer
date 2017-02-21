# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 16:31:37 2015

@author: Joe Vandagriff
"""

from numtheory import isPrime
import itertools

numset = ['1','2','3','4','5','6','7','8','9']
primesinpower = {}
for i in range(5):
    x = itertools.permutations(d,i+1)
    X = filter(isPrime, [int(''.join(a)) for a in x])
    primesinpower[i] = X

for primeSet in primesinpower.values():
    for prime in primeSet:
        l = set(str(prime))