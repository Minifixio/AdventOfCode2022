f = open("./data/d3/input.txt")
l = [ x for x in ''.join(f.readlines()).strip().split('\n') ]

def p1():
    s=0
    for e in l:
        n=len(e)
        c=list(set(e[:n//2])&set(e[n//2:]))[0]
        if ord(c) >= ord('a'): r=ord(c)-ord('a')+1
        else: r=ord(c)-ord('A')+27
        s+=r
    return s

def p2():
    s=0
    for i in range(0,len(l),3):
        c=list(set(l[i])&set(l[i+1])&set(l[i+2]))[0]
        if ord(c) >= ord('a'): r=ord(c)-ord('a')+1
        else: r=ord(c)-ord('A')+27
        s+=r
    return s

p1()
p2()
        