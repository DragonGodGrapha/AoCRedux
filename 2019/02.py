class Computer:
    
    def __init__(self,code,name='Computer',debug=False):
        self.name=name
        self.code=code.copy()
        self.orig=code.copy()
        self.debug=debug
        self.pointer=0
        self.isStopped=False
        self.isFinished=False
    
    def reset(self):
        self.code=self.orig.copy()
        self.pointer=0
        self.isStopped=False
        self.isFinished=False
        
    def toStop(self):
        while not (self.isStopped or self.isFinished):
            self.runCommand()
            
    def setValue(self,index,value):
        self.code[index]=value

    def setPointer(self,value):
        self.pointer=value
        
    def nextValue(self):
        nxt = self.code[self.pointer]
        self.pointer+=1
        return nxt
    
    def decodeC(self,intcode):
        return intcode%100
    
    def decodeP(self,intcode):
        p1=(intcode//100)%10
        p2=(intcode//1000)%10
        p3=(intcode//10000)%10
        return[p1,p2,p3]
    
    def runCommand(self):
        self.command=self.nextValue()
        if self.debug:
            print(f'{self.name} - Index {self.pointer-1}: Command {self.command}')
        if self.decodeC(self.command)==99:
            self.isFinished=True
            if self.debug:print(f'{self.name} - Exiting\n')
            return
        if self.decodeC(self.command)==1:
            self.add()
            return
        if self.decodeC(self.command)==2:
            self.multiply()
            return
        else:
            raise ValueError(f"{self.name} - Unexpected opcode")
    
    
    
    def add(self):
        add1=self.nextValue()
        add2=self.nextValue()
        write=self.nextValue()
        if self.debug:
            print(f'{self.name} - ADD:{self.code[add1]}+{self.code[add2]} to index {write}\n')
        value=self.code[add1]+self.code[add2]
        self.setValue(write,value)
    
    def multiply(self):
        mul1=self.nextValue()
        mul2=self.nextValue()
        write=self.nextValue()
        if self.debug:
            print(f'{self.name} - MUL:{self.code[mul1]}*{self.code[mul2]} to index {write}\n')
        value=self.code[mul1]*self.code[mul2]
        self.setValue(write,value)
    
from itertools import product

import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('02','split',splitval=',',ints=True)

com=Computer(inp,name='cm',debug=True)
com.setValue(1,12)
com.setValue(2,2)

com.toStop()
partA=com.code[0]
pbOut=19690720

for n,v in product(range(100),repeat=2):
    com.reset()
    com.setValue(1,n)
    com.setValue(2,v)
    com.toStop()
    partBValue=com.code[0]
    if partBValue==pbOut:
        break
    
partB=100*n + v

tools.output(partA,partB)