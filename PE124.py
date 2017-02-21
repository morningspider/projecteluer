# -*- coding: utf-8 -*-
"""
Created on Thu Feb 05 11:09:25 2015

@author: Joe Vandagriff
"""

from totient import factorize
import numpy as np
import time

t = time.clock()

def rad(n):
    return np.prod([a for a,b in factorize(n)])

radList = []
for i in range(1,100001):
    radList.append( (i,rad(i))) 

radList = sorted(radList,key=lambda x: x[1])
print radList[9999]
print time.clock() - t