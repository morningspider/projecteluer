# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:29:32 2015

@author: Joe Vandagriff
"""

from numtheory import isPrime
import time

t = time.clock()

a,b,c = {},{},{}
a[0],b[0] = 2,19
hits = [1,2,19]

n = 1

while len(hits) < 2000:
    
    a[n] = 6*n + a[n-1]
    
    if isPrime(6*(n)+5) and isPrime(6*(n)+7) and isPrime(12*(n)+17):
        hits.append(a[n])
    
    b[n] = 6*(n+2) + b[n-1]
    
    if isPrime(6*(n)+11) and isPrime(6*(n)+17) and isPrime(12*(n)+17):
        hits.append(b[n])
        
    n+=1
    
print hits[-1]

print time.clock() - t, "seconds"