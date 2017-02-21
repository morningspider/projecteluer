# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:16:21 2014

@author: Joe Vandagriff
"""

import numpy as np
from decimal import *
count = 0
acc = 0
for i in range(2,100):
    if i not in [1,4,9,16,25,36,49,64,81]:
        getcontext().prec = 102
        x = Decimal(i).sqrt()
        x = list(str(x))
        x.remove('.')
        print len(x)
        acc += np.sum(np.array(x[:100]).astype(int))
        count+=1