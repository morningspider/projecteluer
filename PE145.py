# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 14:07:55 2014

@author: Joe Vandagriff
"""
count = 0
i = 0
while i < 10**9:
    if i%10 == 0:
        i+=1
        continue
    reverse = int(str(i)[::-1])
    s = i + reverse
    for digit in str(s):
        if int(digit)%2 == 0:
            break
    else:
        count+=1
    i+=1
    