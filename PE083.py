# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 15:09:29 2015

@author: Joe Vandagriff
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi
import matplotlib.cm as cmx
import matplotlib.colors as colors
from scipy.spatial.distance import euclidean
theta = np.random.uniform(0,2*pi)
entropy = np.random.uniform(0,1)
#f = open('p083_matrix.txt','r')
#reader = csv.reader(f,delimiter = ',')
#v = []
#for row in reader:
#    v.append(row)
#v = np.array(v,dtype=int)
shape = (100,100)
x_shape,y_shape = shape
v = np.random.rand(*shape)
p = np.zeros(shape)
p[x_shape-1,y_shape-1] = v[x_shape-1,y_shape-1]


indS = {}

for i in range((x_shape + y_shape -1)):
    indS[i] = []
    for k in range(x_shape):
        for j in range(x_shape):
            if j+k == i:
                indS[i].append((j,k))
lines = []
for k in range(x_shape + y_shape - 3,-1,-1):
    for a,b in indS[k]:
        path_coords = []
        paths = []
        for x,y in indS[k+1]:
            if abs(x-a) >1 or abs(y-b)>1:continue
            if a == x or b == y: 
                paths.append(p[x,y])
                path_coords.append(((a,x),(b,y)))
            
            elif a > x:
                s = 0
                for i in range(x,a): s+=v[i,b]
                for j in range(b+1,y): s+=v[x,j]
                s+=p[x,y]
                paths.append(s)
                path_coords.append(((a,x),(b,y)))
            elif a < x:
                s = 0
                for i in range(y,b): s+=v[a,i]
                for j in range(a+1,x): s+=v[j,y]
                s+=p[x,y]
                paths.append(s)
                path_coords.append(((a,x),(b,y)))
        p[a,b] = v[a,b] + min(paths)
        index = np.argmin(paths)
        lines.append(path_coords[index])
            
lines = list(set(lines))

fig, ax = plt.subplots(frameon=False)
plt.axis('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
vmax = euclidean((0,0),(x_shape,y_shape))
my_cmap = cmx.get_cmap('copper')
cNorm  = colors.Normalize(vmin=0, vmax=vmax)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=my_cmap)

for (x,y) in lines:
#    if np.random.uniform(0,1) < entropy: continue
    x1,x2 = x
    y1,y2 = y
    if abs(x1-x2) > 1 or abs(y1-y2) > 1: continue
#    theta = -pi/4
    c_n = np.random.uniform(0,vmax)
    color = scalarMap.to_rgba(c_n)
    newx1 = (x1)*cos(theta) - y1*sin(theta)
    newy1 = (x1)*sin(theta) + y1*cos(theta)
    newx2 = (x2)*cos(theta) - y2*sin(theta)
    newy2 = (x2)*sin(theta) + y2*cos(theta)
    x = (newx1, newx2)
    y = (newy1, newy2)
    ax.plot(x,y,color=color,linewidth=2)
    
plt.show()
    
