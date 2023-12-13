from itertools import permutations
import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('09','lines')

inp=list(map(lambda x: x.split(),inp))
for l in range(len(inp)):
    inp[l]=list(map(int,inp[l]))


def predict(lst,backwards=False):
    nxt=[]
    for i in range(len(lst)-1):
        nxt.append(lst[i+1]-lst[i])
    if set(nxt)=={0}:return lst[-1]
    
    else:
        if not backwards: return lst[-1]+predict(nxt)
        if backwards: return lst[0]-predict(nxt,backwards=True)



predictions=[]
backpredictions=[]
for history in inp:
    predictions.append(predict(history))
    backpredictions.append(predict(history,backwards=True))
partA=sum(predictions)
partB=sum(backpredictions)

tools.output(partA,partB)