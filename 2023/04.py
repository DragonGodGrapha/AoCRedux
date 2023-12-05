from collections import defaultdict

import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('04','lines')

scores=[]
cards=defaultdict(int)



for line in inp:
    temp,card=line.split(' | ')
    cid,win=temp.split(': ')
    cid=int(cid[5:])
    cards[cid]+=1
    card=set(card.split())
    win=set(win.split())
    matches=set.intersection(card,win)
    if matches: scores.append(2**(len(matches)-1))
    for delta in range(len(matches)):
        cards[cid+delta+1]+=cards[cid]
    
    
partA=sum(scores)
partB=sum(cards.values())


tools.output(partA,partB)