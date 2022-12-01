import functools

f = open("./data/d1/input.txt")

def p1():
    l = f.readlines()
    e = ''.join(l).split('\n\n')
    r = list(map(lambda z: functools.reduce(lambda a,b: int(a)+int(b), list(map(int, z.strip().split('\n')))), e))
    return functools.reduce(lambda a,b : a if a>b else b, r)

def p2():
    l = f.readlines()
    e = ''.join(l).split('\n\n')
    r = list(map(lambda z: functools.reduce(lambda a,b: int(a)+int(b), list(map(int, z.strip().split('\n')))), e))
    a,b,c = 0,0,0
    for v in r:
        if v>a:
            b=a
            a=v
        elif v>b:
            c=b
            b=v
        elif v>c:
            c=v
    print(a,b,c)
    return a+b+c

print(p2())
            