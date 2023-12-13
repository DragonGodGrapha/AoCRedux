def openings(char):
    out=[]
    
    if char in ['7','|','F'] :out.append((1,0))
    if char in ['L','J','|'] :out.append((-1,0))
    if char in ['L','F','-'] :out.append((0,1))
    if char in ['J','7','-'] :out.append((0,-1))
    return out
    
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('10','array')

import numpy as np
import networkx as nx

loop={}
sx,sy=np.where(inp=='S')
sy=sy[0]
sx=sx[0]
loop[(sx,sy)]=0
toSearch=[]

if inp[(sx-1,sy)] in ['7','|','F'] :toSearch.append((sx-1,sy))
if inp[(sx+1,sy)] in ['L','J','|'] :toSearch.append((sx+1,sy))
if inp[(sx,sy-1)] in ['L','F','-'] :toSearch.append((sx,sy-1))
if inp[(sx,sy+1)] in ['J','7','-'] :toSearch.append((sx,sy+1))

sShape='.'
if (sx-1,sy) in toSearch and (sx+1,sy) in toSearch:sShape='|'
elif (sx-1,sy) in toSearch and (sx,sy-1) in toSearch:sShape='J'
elif (sx-1,sy) in toSearch and (sx,sy+1) in toSearch:sShape='L'
elif (sx+1,sy) in toSearch and (sx,sy-1) in toSearch:sShape='7'
elif (sx+1,sy) in toSearch and (sx,sy+1) in toSearch:sShape='F'
elif (sx,sy-1) in toSearch and (sx,sy+1) in toSearch:sShape='-'
inp[(sx,sy)]=sShape

for pair in toSearch:
    loop[pair]=1
    
while toSearch:
    current=toSearch.pop(0)
    cx,cy=current
    
    endmodifiers=openings(inp[current])
    for dx,dy in endmodifiers:
        end=(cx+dx,cy+dy)
        
        if end not in loop.keys():
            loop[end]=loop[current]+1
            toSearch.append(end)
partA=max(loop.values())
sizeX,sizeY=inp.shape

sizeX*=3
sizeY*=3
zoomedPipes=np.full((sizeX,sizeY),' ')

for r,v in enumerate(inp):
    for c,ch in enumerate(v):
        zr=r*3 + 1
        zc=c*3 + 1
        if ch!='.' and (r,c) in loop.keys():
            zoomedPipes[(zr,zc)]='x'
            if ch in ['7','|','F'] :zoomedPipes[(zr+1,zc+0)]='x'
            if ch in ['L','J','|'] :zoomedPipes[(zr-1,zc+0)]='x'
            if ch in ['L','F','-'] :zoomedPipes[(zr+0,zc+1)]='x'
            if ch in ['J','7','-'] :zoomedPipes[(zr+0,zc-1)]='x'
            
conn=nx.Graph()

for i,ch in np.ndenumerate(zoomedPipes):
    r,c=i
    if ch==' ':
        if c==0:
            conn.add_edge((r,c),(-1,-1))
        else:
            if zoomedPipes[(r,c-1)]==' ':
                conn.add_edge((r,c),(r,c-1))
                
        if c==sizeY-1:
            conn.add_edge((r,c),(-1,-1))
        else:
            if zoomedPipes[(r,c+1)]==' ':
                conn.add_edge((r,c),(r,c+1))
        if r==0:
            conn.add_edge((r,c),(-1,-1))
        else:
            if zoomedPipes[(r-1,c)]==' ':
                conn.add_edge((r,c),(r-1,c))
                
        if r==sizeX-1:
            conn.add_edge((r,c),(-1,-1))
        else:
            if zoomedPipes[(r+1,c)]==' ':
                conn.add_edge((r,c),(r+1,c))
                
base=(-1,-1)
enclosed=0
exc=nx.algorithms.descendants(conn, (-1,-1))
for i,_ in np.ndenumerate(inp):
    mX,mY=i[0]*3 + 1,i[1]*3 + 1
    if i not in loop.keys() and (mX,mY) not in exc:
        enclosed+=1

partB=enclosed
tools.output(partA,partB)
    