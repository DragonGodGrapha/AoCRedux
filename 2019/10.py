import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('10','lines')
from math import atan2,pi

asteroids=[]
for r,row in enumerate(inp):
    for c,char in enumerate(row):
        if char=='#':
            asteroids.append((c,r))
view={}


for asteroid in asteroids:
    visible=[]
    temp=asteroids.copy()
    temp.remove(asteroid)
    for other in temp:
        dY=other[1]-asteroid[1]
        dX=other[0]-asteroid[0]
        visible.append(atan2(dY,dX))
    view[asteroid]=set(visible)

station,angles=[(k,v) for k,v in view.items() if len(v)==max(list(map(len,view.values())))][0]
partA=len(angles)

angleMap={}
mappedAngles=[]
others=asteroids.copy()

deltasTuple=lambda t:(t[1]-station[1],t[0]-station[0])
rangeTuple=lambda r:abs(r[0]-station[0])+abs(r[1]-station[1])

others.remove(station)

for angle in angles:
    atAngle=[point for point in others if atan2(*deltasTuple(point))==angle]
    angleAdjusted=angle + pi/2
    if angleAdjusted<0:angleAdjusted+=2*pi
    atAngle.sort(key=rangeTuple)
    angleMap[angleAdjusted]=atAngle
    mappedAngles.append(angleAdjusted)
    
index=0
popped=[(-1,-1)]

mappedAngles.sort()

while mappedAngles:
    angle=mappedAngles[index%len(mappedAngles)]
    p=angleMap[angle].pop(0)
    popped.append(p)
    if len(angleMap[angle])==0:
        mappedAngles.remove(angle)
        index-=1
        
    index+=1
result=popped[200]
partB=result[0]*100 + result[1]
tools.output(partA,partB)