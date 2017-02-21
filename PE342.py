# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 10:32:40 2015

@author: Joe Vandagriff
"""

from totient import factorize,primes
from totient import totient3 as phi
from collections import defaultdict

def cubeCheck(n):
    x = [f for f in factorize(n)]
    factors = defaultdict(int)
    for p,exp in x:
        
        factors[p]+= 2*exp-1
        if p == 2: continue
        for p1,exp1 in factorize(p-1):
            factors[p1]+=exp1
    for e in factors.values():
        if e%3 !=0: return False
    return True
    
pList = []
for p in primes():
    if p>10**5: break
    pList.append(p)    
solutions = []
acc = 0 
cubes,squares = [],[]
i = 2
while i**3 < 10**10:
    cubes.append(i**3)
    if i*i < 10**10: squares.append(i*i)
    i+=1
solutions = []

for p in pList:
    if p == 2: continue
    if p > 10: break
    
    x = p*p
    factors = defaultdict(int)
    for p1,exp in factorize(p-1):
        factors[p1]+=exp
    while cubeCheck(x) == False and x < 10**10:
        
        fList = sorted([f for f in factors if factors[f]%3 != 0])
        largeP = fList[-1]
        
        if factors[largeP]%35 == 2: 
            x *= largeP
            factors[largeP] += 1
            for p1,exp in factorize(phi(largeP)):
                factors[p1] += exp
                
            continue
        if factors[largeP]%3 == 1: 
            x *= largeP**3
            factors[largeP] += 2
            for p1,exp in factorize(phi(largeP)):
                factors[p1] += exp
            continue
    otherPrimes = [prime for prime in pList if prime not in factors and prime < p ]
    print factors
    if x < 10**10:
#        print [f for f in factorize(x)]
        for cube in cubes:
            if x*cube > 10**10:break
            if cubeCheck(cube*x): 
                acc+=x*cube
#                print [f for f in factorize(x*cube)]
        for square in squares:
            if x*square > 10**10 or p**2 < square: break
            if cubeCheck(x*square):
                acc+=x*square
                for cube in cubes:
                    if x*cube*square > 10**10:break
                    if cubeCheck(square*cube*x): 
#                        print [f for f in factorize(x*square*cube)]                        
                        acc+=x*cube*square
#        
        