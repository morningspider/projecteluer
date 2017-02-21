# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 10:50:29 2015

@author: Joe Vandagriff
"""

from totient import primes
import time

s = 4
t = time.clock()
i = 1
for p in primes():
    if p < 7: continue
    if p > 10**8: break
    a = ((p**2-1)/24)%p
    xRange = range(p-1,p-5,-1)
    xRange.append(a)
    n = reduce(lambda x,y: (1+x)*y%p,xRange)
    s += n
print time.clock() - t