# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:49:41 2015

@author: Joe Vandagriff
"""

def checkDivisor(n,x,y):
    if n*x%(x**2+y**2)==0 and n*(-y)%(x**2+y**2) == 0:
        return True
    else:
        return False

s = 0
for n in range(1,10**5):
    for i in range(1,n+1):
        for j in range(0,n+1):
            if checkDivisor(n,i,j):
                if j == 0:s+=i
                if j>0: s+=2*i
print s