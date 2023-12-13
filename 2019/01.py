import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('01','lines',ints=True)

from math import floor

def fuelreq(mass):
    return max(floor(mass/3)-2,0)

fuelreqs=[]
tfr=[]

for part in inp:
    rt=fuelreq(part)
    last=rt
    fuelreqs.append(rt)
    while fuelreq(last)>0:
        last=fuelreq(last)
        rt+=last
    tfr.append(rt)
    
    
partA=sum(fuelreqs)
partB=sum(tfr)

tools.output(partA,partB)
