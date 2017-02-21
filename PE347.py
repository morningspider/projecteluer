# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 11:24:47 2015

@author: Joe Vandagriff
"""
import itertools
from totient import primes
import time

t = time.clock()
maxV = 10000000

pList = [p for p in itertools.takewhile(lambda x: x <=(maxV/2), primes())]

mVals = []
j = 0
for i in range(len(pList)):
    if pList[i]**2 > maxV: break
    for j in range(i+1,len(pList)):
        p1,p2 = pList[i],pList[j]
        if p1*p2 > maxV: continue
        a,b = 1,1
        prods = []
        while (p1**a)*p2 <= maxV:
            b = 1
            while (p1**a)*(p2**b) <= maxV:
                prods.append((p1**a)*(p2**b))
                b+=1
            a+=1
        if prods == []: continue
        mVals.append(max(prods))
print sum(set(mVals))

print time.clock() - t