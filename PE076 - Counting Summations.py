# -*- coding: utf-8 -*-
"""
Created on Tue May 20 12:18:06 2014

@author: Joe Vandagriff
"""

import numpy as np
from collections import defaultdict

def pent(n):
    return ( n*(3*n-1) )/2

p = defaultdict(int)

p[0] = 1
p[1] = 1
def getP(m):
    k = 1
    count = 0    
    while pent(k) <= m:
        print pent(k)
        count += ((-1)**(k-1))*p[m-pent(k)]
        k+=1
    k = -1
    while pent(k) <=m:
        print pent(k)
        count += ((-1)**(k-1))*p[m-pent(k)]
        k-=1
    return count
for i in range(1,101):
    p[i] = getP(i)