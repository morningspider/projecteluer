# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:23:49 2016

@author: Joe Vandagriff
"""

from collections import defaultdict
from fractions import Fraction
from totient import primes

steps = []

plist = defaultdict()
n = 500
for i in range(1,n+1):
    plist[i] = (Fraction(1,n))
    
steps.append(plist)

for step in range(1,15):
    current = defaultdict()
    prev = steps[step-1]
    for i in range(1,n+1):
        
        if i == 1:
            current[i] = prev[2]/2
        
        if i == n:
            current[i] = prev[n-1]/2
        
        if i > 1 and i < n:
            current[i] = prev[i-1]*Fraction(1,2) + prev[i+1]*Fraction(1,2)
    
    steps.append(current)
    
pList = []
for p in primes():
    if p > n: break
    pList.append(p)
cList = [x for x in range(1,n+1) if x not in pList]

prob_vector = []

for step in steps:
    prob_p = 0
    prob_n = 0
    for i in range(1,n+1):
        if i in pList:
            prob_p += step[i]*Fraction(2,3)
            prob_n += step[i]*Fraction(1,3)
        if i in cList:
            prob_p += step[i]*Fraction(1,3)
            prob_n += step[i]*Fraction(2,3)
    prob_vector.append((prob_p,prob_n))

#sequence = [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
sequence = [1,0]
final_p = 1
for prob_tuple in prob_vector:
    if len(sequence) == 0: break
    final_p *= prob_tuple[sequence.pop(0)]
print final_p
    