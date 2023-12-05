import sys
sys.path.append('../')
import utils.tools as tools


inp=tools.process('05','lines')

seatscores=[]
for seat in inp:
    row=seat[:7]
    seat=seat[7:]
    
    row=row.replace('F','0')
    row=row.replace('B','1')
    row=int(row,2)

    seat=seat.replace('L','0')
    seat=seat.replace('R','1')
    seat=int(seat,2)
    
    seatscores.append(8*row + seat)

partA=max(seatscores)

for v in range(min(seatscores),max(seatscores)):
    if v not in seatscores and v+1 in seatscores and v-1 in seatscores:
        partB=v
        break

tools.output(partA,partB)