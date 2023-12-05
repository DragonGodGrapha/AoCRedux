import re
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('02','lines')

possible=[]
powers=[]

pR=re.compile(r'(\d+(?= r))')
pG=re.compile(r'(\d+(?= g))')
pB=re.compile(r'(\d+(?= b))')
    
rt,gt,bt=(12,13,14) ##R,G,B
for game in inp:
    red=0
    green=0
    blue=0
  
    gid,rounds=game.split(': ')
    gid=int(gid.split('Game ')[-1])
    red= max(list(map(int,pR.findall(rounds))))
    green= max(list(map(int,pG.findall(rounds))))
    blue= max(list(map(int,pB.findall(rounds))))
    if red<=rt and green<=gt and blue<=bt: possible.append(gid)
    powers.append(red*green*blue)
    
partA=sum(possible)
partB=sum(powers)
tools.output(partA,partB)