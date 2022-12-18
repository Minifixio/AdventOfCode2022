f = open("./data/d10/input.txt")
l = [ x for x in ''.join(f.readlines()).strip().split('\n') ]

def p1():
    cycle,X,s=1,1,0
    for e in l:
        arg=e.split(" ")[0]
        if arg=="addx":
            val=int(e.split(" ")[1])
            if cycle+1==20 or (cycle+1-20)%40==0: s+=(cycle+1)*X
            cycle+=2
            X+=val
        else:
            cycle+=1
        
        if cycle==20 or (cycle-20)%40==0: s+=cycle*X
    
    return s
        
p1()