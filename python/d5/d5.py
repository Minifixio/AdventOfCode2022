f = open("./data/d5/input.txt")
l = [ x for x in ''.join(f.readlines()).split('\n') ]

def format_input():
    n,k=0,0
    for i in range(0, len(l)):
        e=l[i]
        if len(e)>1 and e[1]=='1':
            n=len(e.strip().split("  "))
            k=i
            break
    stacks=[ [] for d in range(0,n)]
    for j in range(0,k):
        e=l[j]
        r=[ e[m:m+3] for m in range(0,4*n-1, 4)]
        for h in range(0,n):
            g = r[h][1]
            if g!=' ': stacks[h].append(g)
    return stacks,k

def d1():
    stacks, k=format_input()
    for i in range(k+2, len(l)-1):
        e=l[i].split(" ")
        a,b,c=int(e[1]),int(e[3])-1,int(e[5])-1
        print(stacks)
        t=stacks[b][:a][::-1]
        stacks[b]=stacks[b][a:]
        stacks[c]=t+stacks[c]
    return "".join([ s[0] for s in stacks])
    
d1()