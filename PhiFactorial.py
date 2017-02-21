# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 14:32:57 2015

@author: Joe Vandagriff
"""
from totient import primes
from totient import totient3 as phi
from math import factorial
import itertools
import numpy as np

n = factorial(13)

pList = []

for p in primes():
    if p > 30000000: break
    if n%(p-1) == 0: pList.append(p)
solutions = []
xList = [1]
i = 2
while len(xList) > 0:
    xList = []
    pos = itertools.combinations_with_replacement(pList,i)
    xList.extend([np.prod(x) for x in pos if phi(np.prod(x)) == n])
    solutions.extend(xList)
    n+=1