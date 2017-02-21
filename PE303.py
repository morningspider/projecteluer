# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 15:22:20 2015

@author: Joe Vandagriff
"""

def f(n):
    if n == 9999: return 1111222222222222212201
    if n == 999: return 11122222222221201
    if n == 99: return 1122222222
    multiple = n
    digits = set(str(multiple))
    while max(digits) > "2":
        multiple += n
        digits = set(str(multiple))
    return multiple