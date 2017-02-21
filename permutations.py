# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 14:20:39 2014

@author: Joe Vandagriff
"""

from math import factorial as fact
digits = []
num = 1
for i in range(1,11):
    count = 0
    for j in range(0,10-i):
        if num + fact(10-i) <= 1000000:
            num += fact(10-i)
            count +=1
    digits.append(count)