# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 11:02:39 2015

@author: Joe Vandagriff
"""

n = 1
acc = 1

def deleteZeros(string):
    while string[-1] == "0":
        string = string[:-1]
    return string[-6:]

while n < 1000000000000:
    
    acc *= n
    acc = str(acc)
    acc = int(deleteZeros(acc))
    n+=1
print acc
