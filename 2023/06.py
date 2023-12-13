import time
start = time.time()

from math import sqrt,ceil,floor
import re
from numpy import product

def boatquad(T,D):
    z1=(T+sqrt(T**2 - 4*D))/2
    z2=(T-sqrt(T**2 - 4*D))/2
    if z1==floor(z1):z1=z1-1
    if z2==ceil(z2):z2=z2+1
  
    return floor(z1),ceil(z2)

import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('test','lines')

numWins=[]

pattern=re.compile(r"(\d+)+")
times,distances=inp
timesA=list(map(int,pattern.findall(times)))
distancesA=list(map(int,pattern.findall(distances)))
pairs=zip(timesA,distancesA)

for pair in pairs:
    l,s=boatquad(*pair)
    numWins.append(l-s+1)
partA=product(numWins)
timeB=int(''.join(pattern.findall(times)))
distanceB=int(''.join(pattern.findall(distances)))

lb,sb=boatquad(timeB,distanceB)
partB=l-s+1

tools.output(partA,partB)

end=time.time()
print(f'Executed in {(end-start)*1000}ms')