import re,itertools
from numpy import prod
import sys
from collections import defaultdict

sys.path.append('../')
import utils.tools as tools
inp=tools.process('03','lines')

def countAdjacent(pos):
    running=0
    row,col=pos
    spots=list(itertools.product([-1,0,1],repeat=2))
    spots.remove((0,0))
    for dRow,dCol in spots:
        try:
            if row+dRow<0 or col+dCol<0:continue
            if (not inp[row+dRow][col+dCol].isdigit()) and inp[row+dRow][col+dCol]!='.': return True
        except IndexError: continue
    return False

def findGears(pos):
    gears=[]
    row,col=pos
    spots=list(itertools.product([-1,0,1],repeat=2))
    spots.remove((0,0))
    for dRow,dCol in spots:
        try:
            if row+dRow<0 or col+dCol<0:continue
            if inp[row+dRow][col+dCol]=='*': gears.append((row+dRow,col+dCol))
        except IndexError: continue
    return gears

pattern=re.compile(r'(\d+)')
rt=[]
gearsdict=defaultdict(list)

for row,line in enumerate(inp):
    for num in pattern.finditer(line):
        val=int(num.group())
        s,e=num.span()
        for col in range(s,e):
            part=countAdjacent([row,col])
            if part:break
        if part:
            rt.append(val)
            continue
partA=sum(rt)


for row,line in enumerate(inp):
    for num in pattern.finditer(line):
        surroundingGears=[]
        val=int(num.group())
        s,e=num.span()
        for col in range(s,e):
            surroundingGears+=findGears([row,col])
        for pair in set(surroundingGears):
            gearsdict[pair].append(val)
        
gearratios=[]
for g in gearsdict.values():
    if len(g)==2:
        gearratios.append(prod(g))
        
partB=sum(gearratios)
tools.output(partA,partB)