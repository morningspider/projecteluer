# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 11:30:36 2015

@author: Joe Vandagriff
"""
from fractions import gcd
from math import sqrt

def A_F(x):
    return x/( 1-x-x**2)

def findx(a):
    a,b = ( a+1 - sqrt( (a+1)**2 + 4*a**2)) ,( (-2)*a )
    d = gcd(a,b)
    return a/d,b/d

def fibSol(a):
    return 5*a**2 +2*a + 1

a,b = 1,2
count = 0
while count < 14:
    newA = a+b
    newB = newA +b
    
    a = newA
    b = newB
    print a*b
    count+=1

