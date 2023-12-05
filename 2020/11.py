import itertools
import numpy as np

import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('11','array')



def countAdjacent(pos):
    running=0
    row,col=pos
    spots=list(itertools.product([-1,0,1],repeat=2))
    spots.remove((0,0))
    for dRow,dCol in spots:
        try:
            if row+dRow<0 or col+dCol<0:continue
            if current[row+dRow,col+dCol]=='#':running+=1
        except IndexError: continue
    return running

def countSeen(pos):
    running=0
    row,col=pos
    maxRow,maxCol=current.shape
    
    dirs=list(itertools.product([-1,0,1],repeat=2))
    dirs.remove((0,0))
    
    for dRow,dCol in dirs:
        row,col=pos
        while 0<=row<=maxRow and 0<=col<=maxCol:
            row+=dRow
            col+=dCol
            if row<0 or col<0 or row>=maxRow or col>=maxCol:break
            
            if current[row,col]=='#':
                running+=1
                break
            elif current[row,col]=='L':
                break
    return running


current=inp.copy()
nextState=inp.copy()
stable=False
row,col=current.shape

while not stable:
    for r in range(row):
        for c in range(col):
            score=countAdjacent((r,c))
            if current[r,c]=='L' and score==0: nextState[r,c]='#'
            elif current[r,c]=='#' and score>=4: nextState[r,c]='L'
    
    if np.array_equal(current,nextState):
        stable=True
    current=nextState.copy()


partA=np.count_nonzero(current=='#')


current=inp.copy()
nextState=inp.copy()
stable=False
row,col=current.shape


while not stable:
    for r in range(row):
        for c in range(col):
            score=countSeen((r,c))
            if current[r,c]=='L' and score==0: nextState[r,c]='#'
            elif current[r,c]=='#' and score>=5: nextState[r,c]='L'
    
    if np.array_equal(current,nextState):
        stable=True
    current=nextState.copy()



partB=np.count_nonzero(current=='#')
tools.output(partA,partB)