import re
from collections import defaultdict
import sys
sys.path.append('../')
import utils.tools as tools


inp=tools.process('07','lines')

rules=list(map(lambda x: x.split(" contain "),inp))

searching=['shiny gold bag']
matches=[]
contents=list(r[1] for r in rules)
storage=list(r[0] for r in rules)

while searching:
    active=searching.pop(0)

    for index,content in enumerate(contents):
        if active in content:
            searching.append(storage[index][:-1])
            matches.append(storage[index][:-1])
                
partA=len(set(matches))
                
goal='shiny gold bag'
ruledict=defaultdict(list)
pattern=re.compile(r'([0-9]+) ([a-z\s]* bag)')
for rule in rules:
    parent=rule[0][:-1]
    content=rule[1][:-1].split(', ')
    for c in content:
        if pattern.match(c):
            pair=pattern.findall(c)[0]
            ruledict[parent].append((int(pair[0]),pair[1]))

            
def bagscore(bag):
    global ruledict
    stored=ruledict[bag]
    score=0
    for line in stored:
        score+=line[0]
        score+=line[0]*bagscore(line[1])
    return score

partB=bagscore(goal)
tools.output(partA,partB)

    
    
    