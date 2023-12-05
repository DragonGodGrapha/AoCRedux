import sys
sys.path.append('../')
import utils.tools as tools


from math import prod

inp=tools.process('03','array')

x,y=0,0
partA=0
partB=[]
width=inp.shape[1]
while y<=inp.shape[0]:
    deltaX=3
    deltaY=1
    x=(x+deltaX)%width
    y+=deltaY
    try:inp[y,x]
    except IndexError: break
    
    if inp[y,x]=='#': partA+=1

partB.append(partA)

slopes=[(1,1),(5,1),(7,1),(1,2)]
for deltaX,deltaY in slopes:
    x,y=0,0
    running=0
    
    while y<=inp.shape[0]:
        x=(x+deltaX)%width
        y+=deltaY
        try:inp[y,x]
        except IndexError: break
    
        if inp[y,x]=='#': running+=1
    partB.append(running)
tools.output(partA,prod(partB))