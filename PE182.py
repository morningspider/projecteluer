# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:32:22 2015

@author: Joe Vandagriff
"""

from collections import defaultdict
from numtheory import factors
import time
from modp import modp
from totient import factorize
t = time.clock()
s = 0
p,q = 7 ,17

unconc = defaultdict(bool)
solution = defaultdict(bool)
bases = []

#unconc2 = defaultdict(int)
for i in range(p*q):
    for e in range((p-1)*(q-1)):
        if gcd(e,(p-1)*(q-1)) > 1: continue
        if modp(i,e,p*q) == i:
            unconc[e] +=1

fList = [a for a,b in factorize((p-1)*(q-1))]
#for i in range(p*q):
for e in factors((p-1)*(q-1)):
    if e ==1:continue
    for f in fList:
        if (e+1)%f == 0:
            k = e+1
            bases.append(k)
            while k < (p-1)*(q-1):
                for f in fList:
                    if k%f == 0:
                        k+=e
                        break
                else:
                    solution[k] = True
                    k+=e
            break
print sorted(solution.keys()),bases
for k in [x +1 for x in factors((p-1)*(q-1)) if x+1 not in bases]:
    if k == 2: continue
    m = k
    while m < (p-1)*(q-1):
        solution[m] = False
        m+=k-1
for x in solution:
    if solution[x]:s+=x
A =  [x for x in unconc if unconc[x]==min(unconc.values())]
B =  [x for x in solution if solution[x]==True]
print sorted(list(set(A).difference(set(B)))), 'Undercounted'
print sorted(list(set(B).difference(set(A)))), 'Overcounted'
#        else:
#            if modp(i,e+1,p*q) == i:
#                k = e+1
#                while k < (p-1)*(q-1):
#                    unconc[k] = True
#                    k+=e
#                break
#    print e,sorted(unconc.keys())
#print list(set(solutionList))
#for i in range(2,(p-1)*(q-1)):
#    for f in fList:
#        if i%f == 0:break
#    else:
#        if unconc[i] != True: print i,isPrime(i)
print time.clock()-t
##    