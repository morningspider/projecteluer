# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:36:49 2016

@author: Joe Vandagriff
"""

from totient import *
from fractions import gcd

def rad(n):
    acc = 1
    for (p,exp) in factorize(n):
        acc*=p
    return acc

count = 0
hits = []
for a in range(1,1000):
    for b in range(a,1000):
        if a + b > 120000: break
        
        c = a + b
        if gcd(a,b) > 1: continue
        if gcd(a,c) > 1: continue
        if gcd(b,c) > 1: continue        
        
        if rad(a*b*c) < c:
            hits.append((a,b,c))
            count +=1