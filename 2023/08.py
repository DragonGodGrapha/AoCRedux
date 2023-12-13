from itertools import permutations
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('08','chunk')

curr='AAA'
end='ZZZ'

nav=list(map(lambda x:0 if x=='L' else 1,inp[0][0]))
nodelist=inp[1]
nodes={}

for node in nodelist:
    cell,out=node.split(' = ')
    out=tuple(out[1:-1].split(', '))
    nodes[cell]=out


path=[curr]
idx=0
while curr!=end:
    direction=nav[idx%len(nav)]
    curr=nodes[curr][direction]
    path.append(curr)
    idx+=1

partA=idx



curr=[j for j in nodes.keys() if j[-1]=='A']
cycles=[]
for cell in curr:
    idxB=0
    while cell[-1]!='Z':
        direction=nav[idxB%len(nav)]
        cell=nodes[cell][direction]
        idxB+=1
    cycles.append(idxB)
from math import lcm
partB=lcm(*cycles)


tools.output(partA,partB)
