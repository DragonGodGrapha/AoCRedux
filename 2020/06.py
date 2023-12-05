import sys
sys.path.append('../')
import utils.tools as tools


inp=tools.process('06','chunk')

answersList=[]
for group in inp:
    answers=set(''.join(group))
    answersList.append(answers)
partA=sum(len(g) for g in answersList)

answersB=[]
for group in inp:
    answersB.append(set.intersection(*list(map(set,group))))
    
partB=sum(len(g) for g in answersB)

tools.output(partA,partB)