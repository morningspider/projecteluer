# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:31:48 2015

@author: Joe Vandagriff
"""
import numpy as np
from collections import defaultdict
from itertools import count
import time
from numtheory import factors
from totient import factorize
from totient import totient3 as phi
primes_cache, prime _jumps = [], defaultdict(list)
def primes():
    prime = 1
    for i in count():
        if i < len(primes_cache): prime = primes_cache[i]
        else:
            prime += 1
            while prime in prime_jumps:
                for skip in prime_jumps[prime]:
                    prime_jumps[prime + skip] += [skip]
                del prime_jumps[prime]
                prime += 1
            prime_jumps[prime + prime] += [prime]
            primes_cache.append(prime)
        yield prime



squares,pList = [],[]
squares = np.array([i*i for i in range(10**3)])

powers2 = [2**i for i in range(3,23)]
pow2 = powers2.pop(0)
threeN = []
for p in primes():
    if p > 10**7: break
    pList.append(p)
    if (p+1)%3 == 0 and p>2:
        threeN.append(3*p)

sqStack2 = list(2*np.array(pList[1:])**2)
sqStack3  = list(3*np.array(pList[1:])**2)
sqStack5  = list(5*np.array(pList[1:])**2)
cubeStack2 = list(2*np.array(pList[1:])**3)
pList2 = list(np.array(pList[1:])*2)

prime = pList.pop(0)
prime2 = pList2.pop(0)
sqr2 = sqStack2.pop(0)
sqr3 = sqStack3.pop(0)
sqr5 = sqStack5.pop(0)
cube2 = cubeStack2.pop(0)
threen = threeN.pop(0)
squares = np.array([i*i for i in range(10**6)])

t = time.clock()
n = 2
acc = 0

while n <= 10**5:
    
    if n == prime:
        acc+=1
        prime = pList.pop(0)
#        print n,1
        n+=1
    elif np.sqrt(n).is_integer():
        acc+=1
        n+=1
    elif n == prime2:
        acc+=n/2 + 1
        prime2 = pList2.pop(0) 
        n+=1
    elif n in powers2:
        acc+=1
        pow2 = powers2.pop(0)
        n+=1
#        print n,1 
    elif n == sqr2:
        acc += n/2 + 1
        sqr2 = sqStack2.pop(0)
        n+=1
    elif n == cube2:
        acc += n/2 + 1
        cube2 = cubeStack2.pop(0)
        n+=1
    elif n == threen:
        acc += 2*n/3
        threen = threeN.pop(0)
        n+=1
    elif n == sqr3:
        acc += 2*n/3
        sqr3 = sqStack3.pop(0)
        n+=1
    elif (n-12)%16 ==0:
        acc+= 3*n/4
        n+=1
    else:
        x = squares[:n]%n
        y = np.arange(n)
        bigN = 1
        a = x==y
        if np.sum(a)>0: bigN = np.max(y[a])
        acc+=bigN
#        if n%9 == 3: print n, bigN,bigN/float(n)
        if n == sqr5:        
            sqr5 = sqStack5.pop(0)
            if bigN/(1.0*n) != 0.8:print n, bigN,np.sqrt(n/5),float(bigN)/n
        n+=1

print time.clock() - t