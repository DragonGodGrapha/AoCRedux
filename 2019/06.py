def distance(source,target):
    d=0
    while source!=target:
        d+=1
        source=orbit[source]
    return d

import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('06','lines')


inp=list(map(lambda x:x.split(')'),inp))



orbit={}#Key:Orbiter Object, Value:Orbited
base='COM'
for line in inp:
    orbit[line[1]]=line[0]

distances=[]
for value in orbit.keys():
    distances.append(distance(value,base))
partA=sum(distances)

t1,t2=orbit['YOU'],orbit['SAN']

transfers=0
while t1!=t2:
    d1=distance(t1,base)
    d2=distance(t2,base)
    if d1>=d2:
        t1=orbit[t1]
        transfers+=1
        continue
    elif d1<d2:
        t2=orbit[t2]
        transfers+=1
        continue
    break
partB=transfers


tools.output(partA,partB)