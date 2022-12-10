f = open("./data/d3/input_test.txt")
l = [ x for x in ''.join(f.readlines()).strip().split('\n') ]

def d1():
    s=0
    for e in l:
        n=len(e)
        c=list(set(e[:n//2])&set(e[n//2:]))[0]
        if ord(c) >= ord('a'): r=ord(c)-ord('a')+1
        else: r=ord(c)-ord('A')+27
        s+=r
    return s

d1()        
        