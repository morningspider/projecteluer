# -*- coding: utf-8 -*-
"""
Created on Tue May 20 12:39:35 2014

@author: Joe Vandagriff
"""

from collections import Counter
from collections import defaultdict

Counts = defaultdict(int)
s = defaultdict(int)
j = 1000000000
while j < 10000000000:
    c = Counter(str(j))
    for i in range(1,10):
        Counts[i] += c[str(i)]
        if Counts[i] == j:
            s[i]+=j
    j+=1


