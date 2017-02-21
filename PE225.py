# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 13:35:00 2015

@author: Joe Vandagriff
"""
import time
t = time.clock()

count = 0
odd = 3
while count < 124:
    t1,t2,t3 = 1,1,1
    itercount = 0
    while itercount < 50000:
        newT = sum([t1,t2,t3])%odd
        if newT == 0:
            break
        t1,t2,t3 = t2,t3,newT
        itercount+=1
    if itercount == 50000:
        count+=1
    odd+=2
print odd -2
        
print time.clock()-t
        
