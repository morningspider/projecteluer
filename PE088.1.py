# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:57:15 2015

@author: Joe Vandagriff
"""

import itertools
import numpy as np
from numtheory import factors
from numtheory import isPrime
from numtheory import factorPairs
from collections import defaultdict
import time

t = time.clock()
minimalNum = defaultdict(int)
x = 4

while 11944 not in minimalNum:
    opts = factorPairs(x)
    if opts == []: 
        x+=1
        continue
    for pair in opts:
        p = list(pair)
        newList = []
        for i in range(len(p)):
            if len(factors(p[i])) > 2:
                for [a,b] in factorPairs(p[i]):
                    d = list(p)
                    d.remove(p[i])
                    d.extend([a,b])
                    newList.append(d)
        for group in newList:
            if sorted(group) not in opts:
                opts.append(sorted(group))
    for fList in opts:
        k = np.prod(fList) - sum(fList) +len(fList)
        if k not in minimalNum: 
            minimalNum[k] = x
        if k in minimalNum and minimalNum[k] > x: 
            minimalNum[k] = x
            print k
        
    x+=1

numList = []
for k in range(2,12001):
    if minimalNum[k] == 0: print k
    if minimalNum[k] not in numList:
        numList.append(minimalNum[k])
print sum(numList)
print time.clock() - t, "seconds"