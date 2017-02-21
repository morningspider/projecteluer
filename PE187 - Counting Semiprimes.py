# -*- coding: utf-8 -*-
"""
Created on Tue May 13 12:41:00 2014

@author: Joe Vandagriff
"""
count = 0
for prime in primes:
    dum = primes[(primes >= prime)]
    prList = dum[(dum <= 100000000/prime)]
    count += len(prList)
    if len(prList) == 0: break
