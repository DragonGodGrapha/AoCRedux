import sys
sys.path.append('../')
import utils.tools as tools


inp=tools.process('04','chunk')
inp=list(map(lambda x:' '.join(x),inp))

partA=0
partB=0

req=['byr','iyr','eyr','hgt','hcl','ecl','pid']
opt=['cid']

for passport in inp:
    badval=False
    person={}
    p=passport.split(' ')
    for entry in p:
        k,v=entry.split(':')
        person[k]=v
    if set(person.keys())==set(req) or set(person.keys())==set(req+opt):
        
        partA+=1
        
        yearvalidation=['byr','iyr','eyr']
        for code in yearvalidation:
            try: int(person[code])
            except:
                badval=True
                continue
        if badval:continue
        
        if not 1920<=int(person['byr'])<=2002:
            continue
        if not 2010<=int(person['iyr'])<=2020:
            continue
        if not 2020<=int(person['eyr'])<=2030:
            continue
        
        if person['hgt'][-2:] in ['cm','in']:
            unit=person['hgt'][-2:]
            value=person['hgt'][:-2]
            try: value=int(value)
            except:continue
            if unit=='in' and not 59<=value<=76:continue
            if unit=='cm' and not 150<=value<=193:continue            
        else:continue
        
        if not (person['hcl'][0]=='#' and set(person['hcl'][1:]).issubset(set('1234567890abcdef'))):
            continue
        if not person['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            continue
        
        if len(person['pid'])==9:
            try: int(person['pid'])
            except: continue
        else: continue
        
        partB+=1
        
tools.output(partA,partB)
            