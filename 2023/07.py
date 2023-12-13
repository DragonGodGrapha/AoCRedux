def getTier(hand):
    unique=set(hand)
    for char in unique:
        count=[hand.count(char) for char in unique]
    
    if len(unique)==5:
        return 0#High Card
    if len(unique)==4:
        return 1#One Pair
    if len(unique)==3 and max(count)==2:
        return 2#two pair
    if len(unique)==3 and max(count)==3:
        return 3#Three of
    if len(unique)==2 and max(count)==3:
        return 4#Full House
    if len(unique)==2 and max(count)==4:
        return 5#Four of        
    if len(unique)==1:
        return 6#Five of
    return -1

def getTierWC(hand):
    cards=['2','3','4','5','6','7','8','9','T','Q','K','A']
    if 'J' in hand:
        tiers=[]
        for wild in cards:
            test=hand.replace('J',wild,1)
            tiers.append(getTierWC(test))
        return max(tiers)
        
    else:
        return getTier(hand)
    
def parseHand(hand,wc=False):
    rl=[]
    for char in hand:
        if char.isnumeric():rl.append(int(char))
        elif char=='T':rl.append(10)
        elif char=='J':
            if wc: rl.append(1)
            else: rl.append(11)
        elif char=='Q':rl.append(12)
        elif char=='K':rl.append(13)
        elif char=='A':rl.append(14)
    return rl

def makeHand(lst):
    rs=''
    for val in lst:
        if 1<val<10:rs+=str(val)
        elif val==10:rs+='T'
        elif val==11 or val==1:rs+='J'
        elif val==12:rs+='Q'
        elif val==13:rs+='K'
        elif val==14:rs+='A'
    return rs



import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('07','lines')

hands=[]
bids={}
tiers={}
rank=[]
score=[]
for line in inp:
    hand,bid=line.split()
    hands.append(hand)
    bids[hand]=int(bid)
    tiers[hand]=getTier(hand)

for v in range(min(tiers.values()),max(tiers.values())+1):
    curr=[h for h,t in tiers.items() if t==v]
    curr=list(map(parseHand,curr))
    curr.sort()
    curr=list(map(makeHand,curr))
    rank+=curr

for r,h in enumerate(rank):
    score.append((r+1)*bids[h])
partA=sum(score)

tiersB={}
rankB=[]
scoreB=[]
for hand in hands:
    tiersB[hand]=getTierWC(hand)
    
for v in range(min(tiersB.values()),max(tiersB.values())+1):
    curr=[h for h,t in tiersB.items() if t==v]
    curr=list(map(lambda x: parseHand(x,True),curr))
    curr.sort()
    curr=list(map(makeHand,curr))
    rankB+=curr

for r,h in enumerate(rankB):
    scoreB.append((r+1)*bids[h])
partB=sum(scoreB)

tools.output(partA,partB)
