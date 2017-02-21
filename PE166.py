# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 16:20:39 2015

@author: Joe Vandagriff
"""

import itertools
import numpy as np
x = range(10)

rows = list(set([row for row in itertools.combinations_with_replacement(x,4)]))
rowPerms = []

for row in rows:
    rowPerms += list(set([x for x in itertools.permutations(row)]))
sVal = {}
for k in range(7):
    sVal = filter(lambda x: sum(x) == k,rowPerms)
    count = 0
    for row1 in sVal[:len(sVal)/2+1]:
        for row2 in sVal:
            if row1[0] + row2[0] > k:continue
            if row1[1] + row2[1] > k:continue
            if row1[2] + row2[2] > k:continue
            if row1[3] + row2[3] > k:continue            
            if row1[0] + row2[1] > k:continue
            if row1[3] + row2[2] > k:continue
            for row3 in sVal:
                if row1[0] + row2[0] + row3[0] > k:continue
                if row1[1] + row2[1] + row3[1] > k:continue
                if row1[2] + row2[2] + row3[2] > k:continue
                if row1[3] + row2[3] + row3[3] > k:continue            
                if row1[0] + row2[1] + row3[2] > k:continue
                if row1[3] + row2[2] + row3[1] > k:continue
                for row4 in sVal:
                    
                    if row1[0] + row2[0] + row3[0] + row4[0] != k:continue
                    if row1[1] + row2[1] + row3[1] + row4[1] != k:continue
                    if row1[2] + row2[2] + row3[2] + row4[2] != k:continue
                    if row1[3] + row2[3] + row3[3] + row4[3] != k:continue            
                    if row1[0] + row2[1] + row3[2] + row4[3] != k:continue
                    if row1[3] + row2[2] + row3[1] + row4[0] != k:continue
                    count+=1
#                    print row1
#                    print row2
#                    print row3
#                    print row4
#                    print

    print k,count,len(sVal)               

