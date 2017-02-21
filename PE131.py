# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:29:50 2016

@author: Joe Vandagriff
"""

from numth import isPrime
from totient import *
from fractions import gcd
from math import sqrt

def factor(n):
    facts = []
    for i in range(1, int(sqrt(n)+1)):
        if n%i == 0:
            facts.extend([i, n/i])
    return sorted(facts)




#for prime in primes():
#    if prime > 2000: break
#    for n in cubes:
#        if  n > prime**3: continue
#        candidate = n*n*(n + prime)
#        for cube in cubes:
#            if candidate < cube: break
#            if candidate == cube: 
##                print prime, n, round(candidate**(1.0/3))
#                print cube/(n*n), n
#                break
##            
p, count, i = 0, 0,0
while count < 10000:
    i+=1    
    n = i**3
    factors = factor(n)
    for f in factors:
        x = n + f
        if x%f !=0: continue
        if x/f == n/f+1 and (x**3)%n**2 == 0: 
            p = (x**3)/(n*n) - n
            if isPrime(p) and p < 1000000 and x**3 == n**2*(n+p): 
                print  n, p, x
                count+=1
                break
            
#    
#for n in cubes:
#    for n in cubes:
#        if n > 1 and n >= cube/(n*n): break
#        if cube % (n*n) != 0: continue
#        if isPrime(cube/(n*n) - n): 
#            x = int(round(cube**(1.0/3)))
#            g = gcd(x,n)
#            print n, x, cube/(n*n) - n, n/g, x/g
#            break
#            
        