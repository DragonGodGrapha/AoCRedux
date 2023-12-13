def solve(report: str,pattern: tuple[int],currentMatchLength=0) -> int:
    key=(report,pattern,currentMatchLength)
    
    # ADAPTED FROM FUNCTION BY https://github.com/mebeim/aoc/
    
    if key in CACHE:
        return CACHE[key]
    
    if len(pattern)==0: #No more pattern to match
        if '#' in report: #Can't match, automatically fails
            return 0
        else: #Matches with all ?=>., only 1 way
            return 1
    
    if currentMatchLength>pattern[0]: #Too many # in current length
        return 0
    
    if not report: #Empty string, have gone through all characters
        
        if len(pattern)==1 and currentMatchLength==pattern[0]: #On last group and length matches
            return 1
        return 0 #Too many pattern left, or last group isn't matched yet
    
    char=report[0] #First character of report
    total=0 #Number of possible arrangements
    if char in ['#','?']: #If first character is #, same group continues
        total+=solve(report[1:],pattern,currentMatchLength+1)
    if char in ['.','?']: #If first character is ., move to next group
        
        if currentMatchLength==0: #Not started next group, don't remove the group yet            
            total+=solve(report[1:],pattern,0)
            
        elif currentMatchLength==pattern[0]:##Just ended group, move to next group if it matches
            total+=solve(report[1:],pattern[1:],0)
        
            
    CACHE[key]=total
    return total
    
    
    
import sys,re
sys.path.append('../')
import utils.tools as tools
inp=tools.process('12','lines')
inp=list(map(lambda x:x.split(),inp))    

CACHE={}
regex=re.compile(r'(#+)+')
count=[]
countB=[]
index=0
l=len(inp)
for pattern,order in inp:
    order=tuple(map(int,order.split(',')))
    patternSolution=solve(pattern,order)
    count.append(patternSolution)
    patternSolutionB=solve('?'.join([pattern]*5),order*5)
    countB.append(patternSolutionB)
partA=sum(count)
partB=sum(countB)
tools.output(partA,partB)