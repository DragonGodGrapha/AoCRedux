import re

import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('01','lines')       

numbers=[]
for line in inp:
    running=0
    for char in line:
        try:
            running+=10*int(char)
        except ValueError: continue
        break
        
    for char in reversed(line):
        try:
            running+=int(char)
        except ValueError: continue
        break
    numbers.append(running)
partA=sum(numbers)



pattern=re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d)+?)')
numbersDict={'one':1,'1':1,'two':2,'2':2,'three':3,'3':3,'four':4,'4':4,'five':5,'5':5,'six':6,'6':6,
         'seven':7,'7':7,'eight':8,'8':8,'nine':9,'9':9}
bNumbers=[]
i=0
for line in inp:
    running=0
    matches=pattern.findall(line)
    running+=numbersDict[matches[0]]*10
    running+=numbersDict[matches[-1]]
    
    bNumbers.append(running)
    i+=1
partB=sum(bNumbers)

tools.output(partA,partB)
