# -*- coding: utf-8 -*-
"""
Created on Wed May 21 13:39:57 2014

@author: Joe Vandagriff
"""

from numtheory import divisors

def solutions(n):
    return (divisors(n**2)+1)/2
n =2
count = 0
while count < 1000:
    if n%3 !=0:
        n+=2
        continue
    if n%5 != 0:
        n+=2
        continue
    count = solutions(n)
    n+=2
print n-1