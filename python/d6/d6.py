f = open("./data/d6/input.txt")
l = f.readline().strip()

def d1():
    n=len(l)
    for i in range(n-3):
        c=l[i:i+4]
        if c.count(c[0])==1 and c.count(c[1])==1 and c.count(c[2])==1 and c.count(c[3])==1:
            return (i+4)
            

d1()