# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 12:30:27 2015

@author: Joe Vandagriff
"""

def removeSheet(Env,i):
    sheet = Env.pop(i)
    if sheet == 8:
        Env.append(4)
        Env.append(2)
        Env.append(1)
    if sheet == 4:
        Env.append(2)
        Env.append(1)
    if sheet == 2:
        Env.append(1)
    return sorted(Env)


probs = {}

probs[ (1,2,4,8) ] = 1
countdown = 15
while countdown > 2:
    for key in probs.keys():
        if sum(key) == countdown:
            keyList = list(key)
            n = len(keyList)
            pr = probs[key]*1.0/n
            for i in range(n):
                dum = keyList[:]
                sheet = tuple(removeSheet(dum,i))
                if sheet in probs.keys():
                    probs[sheet]+=pr
                else:
                    probs[sheet] = pr
    countdown-=1                    
            

