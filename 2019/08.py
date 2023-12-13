from itertools import permutations
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('08','chars')

import numpy as np
dims=(6,25)##Rows,Cols
perLayer=np.product(dims)

layers=[]
layerHelper={}

for chunk in range(len(inp)//perLayer):
    t=np.zeros(dims)
    fill=inp[chunk*perLayer:chunk*perLayer+perLayer]
    for row in range(len(fill)//dims[1]):
        r=fill[row*dims[1]:row*dims[1]+dims[1]]
        t[row][:]=r.copy()
    layers.append(t)
    layerHelper[chunk]=np.count_nonzero(t==0)

minZerosLayer=[k for k,v in layerHelper.items() if v==min(layerHelper.values())][0]
partA=np.count_nonzero(layers[minZerosLayer]==1)*np.count_nonzero(layers[minZerosLayer]==2)

output=[]
for r in range(dims[0]):
    row=[]
    for c in range(dims[1]):
        for l in layers:
            pixel=l[r,c]
            if pixel==2:continue
            elif pixel==1:row.append('█')
            elif pixel==0:row.append(' ')
            break
    output.append(row)
    
output=list(map(lambda x:''.join(x),output))
output='\n'.join(output)
partB='\n\n'+output

tools.output(partA,partB)