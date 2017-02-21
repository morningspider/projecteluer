# -*- coding: utf-8 -*-
"""
Created on Fri May 16 12:36:54 2014

@author: Joe Vandagriff
"""

from math import sqrt
import time

t = time.clock()

m,d,a,A,B = {},{},{},{},{}
largex = 0
largeD = 0
for D in range(2,1001):
    if sqrt(D) == int(sqrt(D)): continue
    m[0] = 0
    d[0] = 1
    a[0] = int(sqrt(D))
    A[0] = a[0]
    B[0] = 1
    k = 1
    while A[k-1]**2 - D*B[k-1]**2 !=1:
        m[k] = d[k-1]*a[k-1] - m[k-1]
        d[k] = (D - m[k]**2)*1.0/d[k-1]
        a[k] = int( (a[0]+m[k])/d[k])
        if k ==1:
            A[1] = a[1]*a[0]+1
            B[1] = a[1]
        if k >1:
            A[k] = a[k]*A[k-1] + A[k-2]
            B[k] = a[k]*B[k-1] + B[k-2]
        k+=1
    print D,A[k-1],B[k-1], A[k-1]*1.0/B[k-1]
    if A[k-1] > largex:
        largex = A[k-1]
        largeD = D
print largez

print time.clock()-t