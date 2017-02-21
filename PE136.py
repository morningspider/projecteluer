# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 11:40:30 2015

@author: Joe Vandagriff
"""
from math import sqrt
from collections import Counter
from totient import primes

#n = 1
#singletons = 0
#while n < 500:
#    k = 1
#    sCount = 0
#    sols = []
#    while k<n/2.0:
#        if 4*k**2 -n <0 :
#            k+=1
#            continue
#        x0 = 3*k + sqrt(4*k**2 - n)
#        x1 = 3*k - sqrt(4*k**2 - n)
#        if x0.is_integer():
#            sCount +=1
#            sols.append([x0,k])
#        if x1 > 2*k and x1.is_integer() and x0 !=x1:
#            sCount +=1
#            sols.append([x1,k])
#        k+=1
#        
##    if sCount == 1:
###        singletons+=1
##        if n%2 == 1:
##            print n, sols,4*sols[0][1]**2,2*sqrt(4*sols[0][1]**2-n)+1
#    if   n%2 == 0 and len(sols)==1 :
#        print n, sols
#    n+=1


pList = primes()
pList.next()
p = 1
count = 0

while p < 50000000:

    if (p+1)%4 == 0: 
        count+=1
    if p*16 < 50000000: 
        count+=1
    if p*4 < 50000000: 
        count+=1
    p = pList.next()
print count