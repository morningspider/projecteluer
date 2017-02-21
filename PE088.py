# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:57:06 2015

@author: Joe Vandagriff
"""
from numpy import prod

def sumsq(n):
    return n*(n+1)*(2*n+1)/6

def isPalindrome(k):
    s = str(k)
    for char in range(0,len(s)/2):
        if s[char] != s[-char-1]:
            return False
    return True
acc = 0
sqList = []
palindromes = []
for n in range(1,10000):
    s = sumsq(n)
    if n>1 and s - sqList[-1] > 100000000: break
    if isPalindrome(s) and 1 < s <100000000:
        palindromes.append(s)
    for sq in sqList[:-1]:
        if isPalindrome(s-sq) and s-sq < 100000000: 
            palindromes.append(s-sq)

    sqList.append(s)
        
print len(palindromes),len(set(palindromes))