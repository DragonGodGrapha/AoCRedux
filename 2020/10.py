from collections import defaultdict
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('10','lines',ints=True)

inp.sort()
inp=[0]+inp+[inp[-1]+3]
diff=[0,0,0,0]

for i in range(len(inp)-1):
    delta=inp[i+1]-inp[i]
    diff[delta]+=1
partA=diff[1]*diff[3]

chain=defaultdict(int)
chain[0]+=1
for val in inp[1:]:
    if val-1 in chain:
        chain[val]+=chain[val-1]
    if val-2 in chain:
        chain[val]+=chain[val-2]
    if val-3 in chain:
        chain[val]+=chain[val-3]
partB=chain[inp[-1]]

tools.output(partA,partB)