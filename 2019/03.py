from collections import defaultdict
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('03','lines')
ch1,ch2=list(map(lambda x:x.split(','),inp))

line1=defaultdict(int)
line2=defaultdict(int)
directions={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

cx,cy=(0,0)
distance=0
for l in ch1:
    length=int(l[1:])
    dx,dy=directions[l[0]]
    for i in range(length):
        cx+=dx
        cy+=dy
        distance+=1
        if not line1[(cx,cy)]:line1[(cx,cy)]=distance

cx,cy=(0,0)
distance=0
for l in ch2:
    length=int(l[1:])
    dx,dy=directions[l[0]]
    for i in range(length):
        cx+=dx
        cy+=dy
        distance+=1
        if not line2[(cx,cy)]:line2[(cx,cy)]=distance

crossings=set(line1.keys()).intersection(set(line2.keys()))
crossingM=[]
crossingR=[]
for pair in crossings:
    crossingM.append(abs(pair[0])+abs(pair[1]))
    crossingR.append(line1[pair]+line2[pair])
    
partA=min(crossingM)
partB=min(crossingR)

tools.output(partA,partB)