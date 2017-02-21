# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:08:11 2015

@author: Joe Vandagriff
"""
import time
from fractions import gcd
from math import factorial
from itertools import combinations_with_replacement
from collections import Counter

t = time.clock()
exp = 0

for k in range(2,8):
    
    p = 0.0
    
    x = [c for c in combinations_with_replacement(range(1,11),k) if sum(c) == 20]
    
    for comb in x:
        num,denom = 1,1
        
        num *= factorial(k)
        cnt = Counter(comb)
        for count in cnt.values():
            denom *= factorial(count)
        
        for a in comb:
            num *= factorial(10)
            denom *= factorial(10-a)*factorial(a)
        num*=factorial(20)
        
        for i in range(20): denom *= 70-i
        
        g = gcd(num,denom)
        num /= g
        denom /= g
        
        p += 1.0*num/denom
        
    p *= factorial(7)/(factorial(k)*factorial(7-k))
    exp += k*p
    
print exp
print time.clock() - t
    
