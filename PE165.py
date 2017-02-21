# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:33:38 2015

@author: Joe Vandagriff
"""

s0 = 290797
endpoints = []

while len(endpoints)< 20000:
    s1 = s0*s0/50515093
    s0 = s1
    t = s0/500
    endpoints.append(t)