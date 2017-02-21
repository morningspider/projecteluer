# -*- coding: utf-8 -*-
"""
Created on Wed May 21 12:17:22 2014

@author: Joe Vandagriff
"""
maxc = 0
count = 0
n = 100000
while count < 1000:
    if n%3 != 0: 
        n+=2
        continue
    if n%5 != 0: 
        n+=2
        continue
    if n%7 != 0:
        n+=2
        continue
    count = 0
    x = n+1
    while x <=2*n:
        if n*x%(x-n)==0:
            count+=1
        x+=1
    if count >1000:
        print n
    if count > maxc: 
        maxc = count
        print n
    n+=2

print n-2