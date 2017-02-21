# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 14:54:22 2015

@author: Joe Vandagriff
"""

from totient import primes
from numtheory import isPrime
from math import floor,log
from collections import defaultdict

Neighbors = {}
pList = {}
primeList = []
for p in primes():
    if p > 10**4: break
    pList[p] = True
    primeList.append(p)

def digitSwap(n,maxN):
    hits = []
    nString = str(n)
    i = 0
#    attempts = [] #debug
    while i < len(nString):
        
        k = 0
        if i == 0: k +=1
        while k < 10:
            if n > 3 and i == len(nString) -1 and k%2 == 0: 
                k+=1
                continue
            p = int(''.join([nString[0:i],str(k),nString[i+1:len(nString)]]))
#            if p < maxN: attempts.append(p) #debug
            if pList.get(p) and p < maxN: 
                hits.append(p)
            k+=1
        i+=1
    if n > 10 and str(n)[1] !='0' and pList.get((int(str(n)[1:]))):
        hits.append(int(str(n)[1:]))
#    print sorted(list(set(attempts))) #debug
    return sorted(list(set(hits)))
fails = []
acc = 0
count = 0
pCount = 0
twoPath = {2:True}
#Neighbors[2] = [2,3,5,7]
for p in sorted(pList.keys()):
    series = []
    series.append(p)
    if p == 2: continue
    if p > 10**4: break
    pCount +=1
    hits = sorted(digitSwap(p,p))
    for k in hits:
        if twoPath.get(k) and k < p:
            twoPath[p] = True
            series.append(k)
#            print p, series
            break
    if twoPath.get(p): continue
    tried = defaultdict(bool)
    while 2 not in hits and twoPath.get(p) != True and len(hits) > 0:
        
#        if count > 5: break
        if tried[hits[0]] == True:
            hits.pop(0)
            continue
        big= hits[0]
        if big >=p:
            hits.pop(0)
            continue
        tried[big] = True
        series.append(big)
        for k in digitSwap(big,p):
            if twoPath.get(k):
                twoPath[p] = True
                series.append(k)
                break
            if tried[k]: continue
            if k not in hits: hits.append(k)
        hits = sorted(list(set(hits)))
#        print p,hits
#        print hits
        hits.remove(big)
        if p in hits: hits.remove(p)
#        count+=1
    
    if 2 in hits:
        twoPath[p] = True
        for number in series:
            if twoPath[number] == None:
                twoPath[number] = True
        series.append(2)
    print p, series
    if 2 not in hits and twoPath.get(p) ==None: 
#        print p
        fails.append(p)
        acc+= p
        count+=1
        
#    Neighbors[p] = hits
#    if p == 127: print sorted(list(set(hits)))
#    for n in hits:
#        if n < p:
#            for prime in Neighbors[n]:
#                if prime < p and prime not in hits:
#                    Neighbors[p].append(prime)
                    
#    Neighbors[p] = sorted(list(set(Neighbors[p])))
#acc = 0
#for p in Neighbors:
#    if Neighbors[p][0] !=2: acc+=p
