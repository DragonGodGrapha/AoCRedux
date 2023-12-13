import sys
sys.path.append('../')
import utils.tools as tools
from utils.modules import Computer
from collections import defaultdict

inp=tools.process('11','split',splitval=',',ints=True)
turtle=Computer(inp,name='TurtleBrain',debug=0)

def move(p,d):
    moves=[(0,1),(1,0),(0,-1),(-1,0)]
    x=p[0]+moves[d][0]
    y=p[1]+moves[d][1]
    return(x,y)
def turn(r,i):
    if i==0:i=-1
    r=(r+i)%4
    return r
'''
#Sense
#Paint
#TurnMove

facing=0 #0N,1E,2S,3W


colors=defaultdict(int)
painted={}

pos=(0,0)
turtle.toStop()


while not turtle.isFinished:
    turtle.io_give(colors[pos])
    color,inst=turtle.output[-2:]
    if color!=colors[pos]:
        colors[pos]=color
        painted[pos]=True
    
    facing=turn(facing,inst)
    pos=move(pos,facing)
partA=len(painted)
'''

turtle.reset()
facingB=0
colorsB=defaultdict(int)
posB=(0,0)
colorsB[posB]=1

turtle.toStop()
while not turtle.isFinished:
    turtle.io_give(colorsB[posB])
    color,inst=turtle.output[-2:]
    if color!=colorsB[posB]:
        colorsB[posB]=color
    
    facingB=turn(facingB,inst)
    posB=move(posB,facingB)

left=min([k[0] for k in colorsB])
right=max([k[0] for k in colorsB])
bottom=min([k[1] for k in colorsB])
top=max([k[1] for k in colorsB])


partB=''
partB+=' '*(1+right-left)+'\n'
for row in range(top,bottom-1,-1):
    rowOut=''
    for col in range(left,right+1):
        color=colorsB[(col,row)]
        if color==1:rowOut+='█'
        else: rowOut+=' '
    rowOut+='\n'
    partB+=rowOut
partB+=' '*(1+right-left)+'\n'
print(partB)