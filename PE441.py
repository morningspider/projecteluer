# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 15:17:29 2015

@author: Joe Vandagriff
"""

from fractions import gcd
import itertools

def lcm(a,b):
    return a*b / gcd(a,b)

def lcmm(*args):
    return reduce(lcm,args)

s=0

for i in range(2,101):
    s_i = 0
    x = range(1,i+1)
    for (a,b) in itertools.combinations(x,2):
        if a+b >=i and gcd(a,b) ==1:
            s_i+=1.0/(a*b)
    print s_i*lcmm(*x),lcmm(*x)
    s += s_i
    