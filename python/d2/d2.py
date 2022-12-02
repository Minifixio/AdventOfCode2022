f = open("./data/d2/input.txt")

def compare(a,b,m,s):
    return ((ord(b)-s) % m) + abs((ord(a)-s+1-((ord(b)-s) % m)) % 3 + ((ord(a)-s+1-((ord(b)-s) % m)) % 3)//2 - 1)*3

def d1(c1, c2):
    m = ord(c2)-ord(c1)-1
    s = ord(c1)
    l = f.readlines()
    e = [ x.split(' ') for x in ''.join(l).strip().split('\n') ]
    r = list(map(lambda z: compare(z[0], z[1], m, s), e))
    return sum(r)

d1('A', 'X')