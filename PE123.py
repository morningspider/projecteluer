# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:14:45 2015

@author: Joe Vandagriff
"""

# Fast exponentiation mod p
import timeit
from totient import primes
t = timeit.time.clock()

def modp(x,y,n):
	acc, s, t = 1, x, y
	while t != 0:
		if (t & 1) == 1: acc = (s*acc)%n
		t = t >> 1
		s = (s**2)%n
	return(acc)
lim = 10**10
pGen = primes()
n = 0
r = 0
while r < lim:
    p = pGen.next()
    n+=1
    a = modp(p-1,n,p*p)
    b = modp(p+1,n,p*p)
    r = (a+b)%(p*p)
print n
print timeit.time.clock()-t