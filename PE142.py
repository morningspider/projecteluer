# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:14:49 2015

@author: Joe Vandagriff
"""

from totient import factorize

def factors(n):
    facts = []
    rt = int(sqrt(n))
    for i in range(1,int(rt)+1):
        if n%i == 0:
            facts.append([i,n/i])

           
    return sorted(facts)

def triples(n):
    triplist = []
    i=1
    while i < n:
        r = 2*i
        for pair in factors((r**2)/2):
            s,t = pair[0],pair[1]
            triplist.append([r+s,r+t,r+s+t])
        i+=1
    return triplist
            