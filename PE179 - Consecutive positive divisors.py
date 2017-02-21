# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:30:20 2014

@author: Joe Vandagriff
"""

def countdiv(n):
    count = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            count +=2
    if sqrt(n) == int(sqrt(n)):
        count-=1
    return count

from numtheory import factors
prev = countdiv(2)
count = 0
for i in range(3,10**7):
    new = countdiv(i)
    if new == prev:
        count+=1
    prev = new
    