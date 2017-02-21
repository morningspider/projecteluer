import csv
import numpy as np
import itertools

f = open('p096_sudoku.txt','r')
reader = csv.reader(f)

def UpdatePossibilities(puzzle):
    poss = []
    for i in range(9):
        rowPoss = []
        for j in range(9):
            if puzzle[i,j] != 0: 
                rowPoss.append([])
                continue
            R = set(puzzle[i])
            C = set(puzzle[:,j])
            S = set(puzzle [ 3*(i/3) : 3*(i/3) + 3, 3*(j/3) : 3*(j/3) + 3 ].flatten())
            rowPoss.append(list(set(range(1,10)) - R - C - S))
        poss.append(rowPoss)
    poss = np.array(poss)
    return poss

def checkRows(puzzle,poss):
    for i,j in itertools.product(range(9),range(9)):
        for item in poss[i,j]:
            for k in range(9):
                if k == j: continue
                if item in poss[i,k]:
                    break
            else: 
                puzzle[i,j] = item
                poss[i,j] = []
                poss = UpdatePossibilities(puzzle)
    return puzzle,poss

def checkCols(puzzle,poss):
    for i,j in itertools.product(range(9),range(9)):
        for item in poss[i,j]:
            for k in range(9):
                if k == i: continue
                if item in poss[k,j]:
                    break
            else: 
                puzzle[i,j] = item
                poss[i,j] = []
                poss = UpdatePossibilities(puzzle)
    return puzzle,poss
    
def checkSqrs(puzzle,poss):
    for i in range(9):
        SqrRow = 3*(i/3)
        for j in range(9):
            SqrCol = 3*(j/3)
            for item in poss[i,j]:
                matchCount = 0
                for k in range(SqrRow,SqrRow +3):
                    for l in range(SqrCol,SqrCol+3):
#                        print "i:",i, " j:",j," k:", k, " l:", l,poss[i,j],poss[k,l]
                        if (k,l) == (i,j): continue
                        if item in poss[k,l]:
                            matchCount += 1
                if matchCount == 0: 
                    puzzle[i,j] = item
                    poss[i,j] = []
                    poss = UpdatePossibilities(puzzle)
    poss = UpdatePossibilities(puzzle)
    return puzzle,poss

def ContradictionCheck(puzzle,poss):
    poss = UpdatePossibilities(puzzle)
    for i in range(9):
        row = puzzle[i][puzzle[i] != 0]
        col = puzzle[:,i][puzzle[:,i] != 0]
        if len(set(row)) < len(row): return False
        if len(set(col)) < len(col): return False
    for i,j in itertools.product(range(9),range(9)):
        if puzzle[i,j] == 0 and len(poss[i,j]) == 0: return False
    for i in range(3):
        for j in range(3):
            sqr = puzzle[3*i:3*i + 3, 3*j:3*j + 3].flatten()
            if len(set(sqr[sqr!=0])) < len(sqr[sqr!=0]): return False
    return True
        

def singleOption(puzzle,poss):
    for i,j in itertools.product(range(9),range(9)):
        if puzzle[i,j] != 0: continue
        if len(poss[i,j]) == 1:
            puzzle[i,j] = poss[i,j][0]
            poss[i,j] = []
            poss = UpdatePossibilities(puzzle)
    return puzzle,poss

def update(puzzle,poss):
    s = np.sum(puzzle == 0)
    changed = True
    while changed == True and s!=0:
        puzzle,poss = singleOption(puzzle,poss)
        puzzle,poss = checkRows(puzzle,poss)
        puzzle,poss = checkCols(puzzle,poss)
        puzzle,poss = checkSqrs(puzzle,poss)
        if np.sum(puzzle == 0) == s:
            changed = False
        s = np.sum(puzzle == 0)
    return puzzle,poss

                
#load puzzles into one big array, cutting out the rows with puzzle names
puzz = []
for row in reader:
    r = row[0]
    if len(r) < 9: continue    
    puzz.append(list(row[0]))


puzzles = []

#initialize puzzles
for i in range(50):
    p = []
    for k in range(9*i,9*i+9):
        p.append(puzz[k])
    puzzles.append(np.array(p).astype(int))
solutions,possibilities = [],[]
#Solving loop, executes once for each puzzle
count = 0
for puzzle in puzzles:
    #initialize possibility array
    poss = UpdatePossibilities(puzzle)
    puzzle,poss = update(puzzle,poss)  
    s = np.sum(puzzle == 0)                               
    if s > 0:
        print count
    possibilities.append(poss)
    solutions.append(puzzle)
    count +=1


            
        