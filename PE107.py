# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 13:36:55 2015

@author: Joe Vandagriff
"""

import csv

f = open('p107_network.txt','r')
reader = csv.reader(f,delimiter = ',')

net = []
i=0
for row in reader:
    net.append(row)
for i in range(40):
    for j in range(40):
        if net[i][j] == '-': net[i][j] = 0
        else: net[i][j] = int(net[i][j])

T = [ [i] for i in range(40)]
sol = [[ 0 for j in range(40)] for k in range(40)]

#Repeat the process until the forest T is one component
while len(T) > 1:
    print len(T[0])

    #iterate through components C of forest T    
    for component in T:
        
        #initialize minimum variables
        minCost = 99999
        minV1 = 99
        minV2 = 99
        #iterate through vertices v in each component C
        for vertex in component[:]:
            
            #iterate through all other vertices
            for i in range(40):
                #isolate the vertices that are outside of C and connected to v
                if i not in component and net[vertex][i]>0:
                    #determine if this vertex is the minimum
                    if net[vertex][i] < minCost:
                        minCost = net[vertex][i]
                        minV1 = i
                        minV2 = vertex
        #debugging check
        if minV1 == 99: 
            print "Error"
        #make a connection at the minumum edge
        sol[minV2][minV1] = net[minV2][minV1]
        for otherC in T:
            if minV1 in otherC:
                component+=otherC
                T.remove(otherC)
        
                    

oldCost = 0
count = 0
for i in range(40):
    for j in range(i+1,40):
        if sol[i][j] >0: count+=1
        oldCost +=net[i][j]
newCost = sum([sum(sol[k]) for k in range(40)])

print oldCost,newCost,oldCost-newCost
                    


