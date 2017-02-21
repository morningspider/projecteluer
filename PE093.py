# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:58:34 2015

@author: Joe Vandagriff
"""

import itertools
def options(a,b,c,d):
    ops = ['+','-','/','*']
    nums = [str(float(x)) for x in [a,b,c,d]]
    
    opList = []
    for comb in itertools.combinations_with_replacement(ops,3):
        for p in itertools.permutations(comb):
            if p not in opList:
                opList.append(p)
    
    numPerm = itertools.permutations(nums)
    vList = []
    for (a,b,c,d) in numPerm:
        for (x,y,z) in opList:
            expList = list([ [a,x,b,y,c,z,d],
                             [a,x,'(',b,y,c,z,d,')'],
                             ['(',a,x,b,y,c,')',z,d],
                             ['(',a,x,b,')',y,'(',c,z,d,')'],
                             ['(',a,x,b,')',y,c,z,d],
                             [a,x,'(',b,y,c,')',z,d], 
                             [a,x,b,y,'(',c,z,d,')'], 
                             [a,x,'(',b,y,'(',c,z,d,')',')'],
                             [a,x,'(','(',b,y,c,')',z,d,')'],
                             ['(',a,x,'(',b,y,c,')',')',z,d],
                             ['(','(',a,x,b,')',y,c,')',z,d],
                             ])
            for exp in expList:
                expStr = "".join(exp)
                try:
                    v = eval(expStr)
                except: continue
                if v > 0 and int(v) == v:
                    if v not in vList: vList.append(v)
    return sorted(vList)

for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                targets = options(a,b,c,d)
                i = 0
                count = 0
                while i+1 <len(targets) and targets[i+1] - targets[i] == 1:
                    count+=1
                    i+=1
                if i > 30:
                    print (a,b,c,d),i+1