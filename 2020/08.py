import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('08','lines')

acc=0
visited=[]
index=0

while index not in visited:
    visited.append(index)
    command,val=inp[index].split(' ')
    val=int(val)
    if command=='acc':
        acc+=val
        index+=1
        continue
    if command=='nop':
        index+=1
        continue
    if command=='jmp':
        index+=val
partA=acc


for i in range(len(inp)):
    broken=False
    copy=inp.copy()
    acc=0
    visited=[]
    index=0
    toChange=copy[i]
    if toChange[:3]=='acc':continue
    if toChange[:3]=='nop':copy[i]='jmp'+toChange[3:]
    else: copy[i]='nop'+toChange[3:]
    
    while index not in visited:
        visited.append(index)
        try: command,val=copy[index].split(' ')
        except IndexError:
            broken=True
            break
        val=int(val)
        if command=='acc':
            acc+=val
            index+=1
            continue
        if command=='nop':
            index+=1
            continue
        if command=='jmp':
            index+=val
    if broken:break
partB=acc
    