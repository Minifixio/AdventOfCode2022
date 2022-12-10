f = open("./data/d4/input.txt")
l = [ x.split(',') for x in ''.join(f.readlines()).strip().split('\n') ]

def p1():
    s=0
    for e in l:
        a=list(map(int,e[0].split('-')))
        b=list(map(int,e[1].split('-')))
        if (a[0]<=b[0] and b[1]<=a[1]) or (b[0]<=a[0] and a[1]<=b[1]):
            s+=1
    return s

def p2():
    s=0
    for e in l:
        a=list(map(int,e[0].split('-')))
        b=list(map(int,e[1].split('-')))
        if (a[0]<=b[0] and b[0]<=a[1]) or (b[0]<=a[0] and a[0]<=b[1]):
            s+=1
    return s

p1()
p2()