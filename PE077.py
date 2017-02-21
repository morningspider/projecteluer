# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 13:27:42 2015

@author: Joe Vandagriff
"""

from totient import primes
from collections import defaultdict
import itertools

m = 60
pList = []

for p in primes():
    if p > m: break
    pList.append(p)
target = 0
while target < 5000:
    pList = []

    for p in primes():
        if p > m: break
        pList.append(p)
    nCount = defaultdict(int)
    for k in range(1, m/2+1):
        for x in itertools.combinations_with_replacement(pList,k):
            if x[0] >= m/k and x[-1] > m/k: break
            nCount[sum(x)] +=1
    target = nCount[m]
    m+=1
print m-1, nCount[m-1]