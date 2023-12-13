import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('05','chunk')
seeds=list(map(int,inp[0][0].split()[1:]))
map1=inp[1][1:]
map2=inp[2][1:]
map3=inp[3][1:]
map4=inp[4][1:]
map5=inp[5][1:]
map6=inp[6][1:]
map7=inp[7][1:]

dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
dict6={}
dict7={}
newseeds=[]
seedsC=seeds.copy()
tr=1
while seedsC:
    start=seedsC.pop(0)
    delta=seedsC.pop(0)
    newseeds+=list(range(start,start+delta))
    print(tr)
    tr+=1

for line in map1:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict1[r]=delta
    
for line in map2:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict2[r]=delta

    
for line in map3:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict3[r]=delta

    
for line in map4:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict4[r]=delta

for line in map5:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict5[r]=delta
    

for line in map6:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict6[r]=delta


for line in map7:
    l=list(map(int,line.split()))
    delta=l[0]-l[1]
    r=range(l[1],l[1]+l[2])
    dict7[r]=delta

    
locations=[]

for seed in seeds:
    d=0
    for k,v in dict1.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict2.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict3.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict4.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict5.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict6.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict7.items():
        if seed in k:
            d=v
    seed+=d

    locations.append(seed)

partA=min(locations)

partB=sys.maxsize
tracker=1
lt=len(newseeds)
for seed in newseeds:
    if tracker%1000000==0: print(str(100*tracker/lt)[:5])
    
    
    d=0
    for k,v in dict1.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict2.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict3.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict4.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict5.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict6.items():
        if seed in k:
            d=v
    seed+=d
    
    d=0
    for k,v in dict7.items():
        if seed in k:
            d=v
    seed+=d

    if seed<partB:
        partB=seed
        print(partB)
    tracker+=1
    

'''
for seed in range(100):
    for k,v in dict1.items():
        if seed in k:
            d=v
    print(f'{seed} - {seed+d}')
    '''

tools.output(partA,partB)