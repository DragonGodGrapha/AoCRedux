import time
start = time.time()

import re
import sys
from numpy import product

sys.path.append('../')
import utils.tools as tools
inp=tools.process('06','lines')

numWins=[]

pattern=re.compile(r"(\d+)+")
times,distances=inp
timesA=list(map(int,pattern.findall(times)))
distancesA=list(map(int,pattern.findall(distances)))
pairs=zip(timesA,distancesA)
distance=lambda t,T:t*(T-t)

for T,D in pairs:
    running=0
    for t in range(T+1):
        d=distance(t,T)
        if d>D:running+=1
    numWins.append(running)
partA=product(numWins)

timeB=int(''.join(pattern.findall(times)))
distanceB=int(''.join(pattern.findall(distances)))

partB=0
for t in range(timeB+1):
    d=distance(t,timeB)
    if d>distanceB:partB+=1

tools.output(partA,partB)

end=time.time()
print(f'Executed in {(end-start)*1000}ms')