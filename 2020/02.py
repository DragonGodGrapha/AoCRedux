import sys
sys.path.append('../')
import utils.tools as tools

inp=tools.process('02','lines')

partACount=0
partBCount=0

for line in inp:
    policy,password=line.split(': ')
    policyNums,policyKey=policy.split(' ')
    policyMin,policyMax=list(map(int,policyNums.split('-')))
    
    if policyMin<=password.count(policyKey)<=policyMax:partACount+=1
    if (policyKey==password[policyMin-1])^(policyKey==password[policyMax-1]):partBCount+=1

tools.output(partACount,partBCount)