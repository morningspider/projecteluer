# -*- coding: utf-8 -*-
"""
Created on Wed May 21 11:20:39 2014

@author: Joe Vandagriff
"""

i = 1

def reverse(n):
    lst = list(str(n))
    return int("".join(lst[::-1]))

def isReversible(n):
    if n%10 == 0:
        return False
    m = n + reverse(n)
    for num in list(str(m)):
        if int(num)%2 == 0:
            return False
    else:
        return True



while i < 1000000000:
    if isReversible(i):
        count+=1
    i+=1
print count