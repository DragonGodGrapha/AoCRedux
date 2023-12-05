import numpy as np
"""
import sys
sys.path.append('../')
import utils.tools as tools
"""

def process(day,mode='lines',splitval='',ints=False):
    with open(str(day)+'.txt') as inputVals:
        if mode=='lines':
            inp=inputVals.read().splitlines()
            if ints: inp=list(map(int,inp))
            
        elif mode=='split':
            inp=inputVals.read().split(splitval)
            if ints: inp=list(map(int,inp))
            
        elif mode=='chunk':
            inp=list(map(str.splitlines,inputVals.read().split('\n\n')))
            if ints:
                for i,line in enumerate(inp):
                    inp[i]=list(map(int,line))
                
            
        elif mode=='array':
            
            lines=inputVals.read().splitlines()
            width=max(list(map(len,lines)))
            height=len(lines)
            inp=np.full((height,width),None)
            for row in range(height):
                line=lines[row]
                for col in range(len(line)):
                    inp[row,col]=line[col]
            def tryint(val):
                if type(val)==int:return int(val)
                else: return val
            intall=np.vectorize(tryint)
            if ints: intall(inp)
            
        
    return inp

def output(partA,partB):
    print(f'Part 1: {partA}')
    print(f'Part 2: {partB}')
