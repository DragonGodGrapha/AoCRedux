import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('11','lines')
inp=list(map(list,inp))

def biRange(a,b):
    if b<a:a,b=b,a
    l=list(range(a,b+1))
    return(l)

from itertools import product


rows=len(inp)
cols=len(inp[0])
voidrows=[]
voidcols=[]

for r in range(rows-1,-1,-1):
    row=inp[r]
    if set(row)=={'.'}:
       voidrows.append(r)


for c in range(cols-1,-1,-1):
    column=tools.columnExtract(inp,c)
    if set(column)=={'.'}:
        voidcols.append(c)


galaxies=[]
for r in range(rows):
    for c in range(cols):
        if inp[r][c]=='#':galaxies.append((r,c))
pairs=product(galaxies,repeat=2)

distances=[]
longdistances=[]
for a,b in pairs:
    x1,y1=a
    x2,y2=b
    dX=biRange(x1,x2)
    dY=biRange(y1,y2)
    emptyX=len(set(voidrows).intersection(set(dX)))
    emptyY=len(set(voidcols).intersection(set(dY)))
    
    d=abs(x1-x2)+abs(y1-y2)
    distances.append(d+1*(emptyX+emptyY))
    longdistances.append(d+999999*(emptyX+emptyY))
partA=sum(distances)//2
partB=sum(longdistances)//2
tools.output(partA,partB)


