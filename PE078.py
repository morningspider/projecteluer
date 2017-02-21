# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:36:36 2015

@author: Joe Vandagriff
"""

from collections import defaultdict

def penta(k):
    return k*(3*k-1)/2
def pentb(k):
    return k*(3*k+1)/2

p = defaultdict(int)
p[0],p[1] = 1,1

n = 2
while p[n-1]%1000000 != 0:
    k = 1
    while penta(k) <= n:
        p[n]+=((-1)**(k-1))*p[n-penta(k)]
        p[n]+=((-1)**(k-1))*p[n-pentb(k)]
        k+=1
    n+=1
