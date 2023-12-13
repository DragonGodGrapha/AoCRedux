import numpy as np
import warnings
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
            
        elif mode=='chars':
            inp=inputVals.read()
            return [v for v in inp]
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



def columnExtract(lst,pos):
    return [x[pos] for x in lst]

def columnReplace(lst,col,pos):
    ##RUNS ON EXISTING LIST
    for r,v in enumerate(col):
        lst[r][pos]=v
        
def columnInject(lst,col,pos):
    ##RUNS ON EXISTING LIST
    if type(col)==str:col=list(col)
    for r,v in enumerate(col):
        row=lst[r][:pos]
        row.append(v)
        row+=lst[r][pos:]
        lst[r]=row

def columnRemove(lst,pos):
    ##RUNS ON EXISTING LIST
    for r in range(len(lst)):
        row=lst[r][:pos]+lst[r][pos+1:]
        lst[r]=row

def cycleBack(lst):
    ##RUNS ON EXISTING LIST
    t=lst[0]
    lst[:-1]=lst[1:]
    lst[-1]=t

def cycleForward(lst):
    ##RUNS ON EXISTING LIST
    t=lst[-1]
    lst[1:]=lst[:-1]
    lst[0]=t

def wildcardSub(pattern,wildcardChar,substitutes):
    patterns=[]
    
    if wildcardChar in pattern:
        subs=[]
        for sub in substitutes:
            if wildcardChar in sub:
                warnings.warn(f"Wildcard character in substitute {sub}. Ignoring value.")
                substitutes.remove(sub)
                continue
            subs.append(pattern.replace(wildcardChar,sub,1))
        for p in subs:
            patterns+=wildcardSub(p,wildcardChar,substitutes)
    else:
        patterns.append(pattern)
    return patterns if type(patterns)==list else [patterns]
