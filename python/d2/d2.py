f = open("./data/d2/input.txt")

def compare1(a,b,m,s):
    return ((ord(b)-s) % m) + abs((ord(a)-s+1-((ord(b)-s) % m)) % 3 + ((ord(a)-s+1-((ord(b)-s) % m)) % 3)//2 - 1)*3

def compare2(a,b,m,s):
    f = ((2*((ord(b)-s) % m))%3 + ((ord(a)-s)%m - (ord(b)-s)%m + 2))%3
    if f==0: f=3
    return f + ((ord(b)-s)%m-1)*3
    
def d1(c1, c2):
    m = ord(c2)-ord(c1)-1
    s = ord(c1)
    l = f.readlines()
    e = [ x.split(' ') for x in ''.join(l).strip().split('\n') ]
    r = list(map(lambda z: compare1(z[0], z[1], m, s), e))
    return sum(r)

def d2(c1, c2):
    m = ord(c2)-ord(c1)-1
    s = ord(c1)
    l = f.readlines()
    e = [ x.split(' ') for x in ''.join(l).strip().split('\n') ]
    r = list(map(lambda z: compare2(z[0], z[1], m, s), e))
    return sum(r)

d1('A','X')
d2('A','X')