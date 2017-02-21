# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 10:11:50 2015

@author: Joe Vandagriff
"""

from totient import primes
from totient import totient3 as phi
from PE248 import inversePhi
from collections import defaultdict

#for p in primes():
#    if p > 40000000: break
#    pList.append(p)

chainLength = defaultdict(list)
chainLength[2] = [2]
chain = 20

while chain < 10:
    for n in list(set(chainLength[chain])):
        if n > 40000000: continue
        for k in inversePhi(n):
            if k%2 == 1: continue
            if k > 40000000: continue
            chainLength[chain+1] += [k]
    if chain >14:
        print 17476 in chainLength[15]
    chain+=1

