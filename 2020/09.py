import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('09','lines',ints=True)

prLength=25
index=25
valid=True
while valid:
    source=inp[index-prLength:index]
    target=inp[index]
    while source:
        test=source.pop()
        if target-test in source:
            break
        if not source:valid=False
    index+=1
partA=target

bIndex=0
uIndex=0
running=0
found=False
while not found:

    running+=inp[uIndex]
    if running>target:
        bIndex+=1
        uIndex=bIndex
        running=0
        continue
    if running==target:
        break
    
    uIndex+=1
contiguous=inp[bIndex:uIndex+1]
partB=min(contiguous)+max(contiguous)
    
    