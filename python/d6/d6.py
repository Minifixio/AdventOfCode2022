f = open("./data/d6/input.txt")
l = f.readline().strip()

def p1():
    n=len(l)
    for i in range(n-3):
        c=l[i:i+4]
        if c.count(c[0])==1 and c.count(c[1])==1 and c.count(c[2])==1 and c.count(c[3])==1:
            return (i+4)

def p2():
    n=len(l)
    for i in range(n-13):
        c=l[i:i+14]
        t=[ c.count(x) for x in c ]
        if t==[1]*14:
            return (i+14)
            

p1()
p2()