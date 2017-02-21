# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:52:03 2016

@author: Joe Vandagriff
"""

def check(n):
    while n > 0:
        d = n%10
        n/=10
        if d >2: return False
    return True


def f(n):
    S = 0
    s = n
    c = 1
    while check(s) == False:
        s+=n
        c+=1
    return c
#    
#
#for i in range(1,10001):
#    if i%99 ==0 or i% 999==0 or i == 9999: continue
#
#    