import sys
sys.path.append('../')
import utils.tools as tools

inp=tools.process('01','lines',ints=True)

goal=2020

partA=inp.copy()
for _ in range(len(partA)):
    valueA=partA.pop()
    target=goal-valueA
    if target in partA:
        partAValue=target*valueA
        break

partB=inp.copy()
for _ in range(len(partB)):
    valueB=partB.pop()
    midTarget=goal-valueB
    partBMidway=partB.copy()
    for _ in range(len(partBMidway)):
        midValue=partBMidway.pop()
        endTarget=midTarget-midValue
        if endTarget in partBMidway:
            partBValue=endTarget*midValue*valueB
            break

tools.output(partAValue,partBValue)