# -*- coding: utf-8 -*-
"""
Created on Mon May 19 13:11:10 2014

@author: Joe Vandagriff
"""

from collections import defaultdict
from fractions import gcd

triples = defaultdict(list)
counts = defaultdict(int)

def triple(k,m,n):
    return 2*k*m*(m+n)

for m in range(1,2000):
    for n in range(1,m):
        if gcd(m,n) > 1:
            continue
        k = 1
        while triple(k,m,n) < 1500000:
            L = triple(k,m,n)
            a = k*(m**2 - n**2)
            b = k*(2*m*n)
            if sorted([a,b]) not in triples[L]:
                triples[L].append(sorted([a,b]))
                counts[L]+=1
            k+=1
            