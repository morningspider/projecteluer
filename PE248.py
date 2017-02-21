# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:19:20 2015

@author: Robert Voorheis
"""
from totient import primes
from numtheory import isPrime,factors
from collections import defaultdict
from math import factorial
import time


t = time.clock()

#all primes for which p-1 divides n!

#match each power of primes with their totient value
def inverPhi(max_phi,max_prime):
    invPhi = defaultdict(list)
    target = 500
    for p in primes():
    
        if p > 5000: break
        i = 1
        a = p-1
        while a <= target:
            a = p**(i-1)*(p-1)
            invPhi[a] += [p**i]
                
            for b in sorted(invPhi.keys()):
                if a*b > target:break
                for x in invPhi[b]:
                    if x%p !=0:
                        invPhi[a*b] += [x*(p**i)]
                                
            i+=1
    return invPhi
            
            

#print inversePhi(factorial(13))[149999]
#print time.clock() - t