# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 15:56:03 2015

@author: Joe Vandagriff
"""
from time import clock

t = clock()

p,q = {0:3},{0:2}
n = 1
a = 0
while a < 10**12:
    p[n] = p[n-1] + 2*q[n-1]
    q[n] = p[n-1] + q[n-1]
    
    if n%2 == 0:
        a = 2*q[n-1]*q[n]
        b = q[n-1]*p[n]
    if n%2 == 1:
        a = p[n-1]*p[n]
        b = p[n-1]*q[n]
    n+=1
print b
print clock() - t

