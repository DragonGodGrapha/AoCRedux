import sys
sys.path.append('../')
import utils.tools as tools
inp=tools.process('04','split',splitval='-',ints=True)

partA=0
partB=0
digits=['1','2','3','4','5','6','7','8','9','0']
for p in range(inp[0],inp[1]+1):
    password=str(p)
    double=False
    strictDouble=False
    incr=True
    for i in range(len(password)-1):
        if int(password[i])>int(password[i+1]):
            incr=False
            break
    if not incr:continue
    
    for d in digits:
        if d*2 in password: double=True
        if d*2 in password and not d*3 in password: strictDouble=True
        if double and strictDouble:break

    if double:partA+=1
    if strictDouble: partB+=1

tools.output(partA,partB)