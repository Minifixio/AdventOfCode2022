f = open("./data/d9/input.txt")
l = [ x for x in ''.join(f.readlines()).strip().split('\n') ]

def movement(t_pos, h_pos):
    res=t_pos
    if h_pos[1]>t_pos[1]+1:
        res[1]+=1
        res[0]=h_pos[0]
    if h_pos[1]<t_pos[1]-1:
        res[1]-=1
        res[0]=h_pos[0] 
    if h_pos[0]>t_pos[0]+1:
        res[0]+=1
        res[1]=h_pos[1]
    if h_pos[0]<t_pos[0]-1:
        res[0]-=1
        res[1]=h_pos[1]
    
    return res

def p1():
    t_map={}
    h_pos=[0,0]
    t_pos=[0,0]
    for e in l:
        d=e.split(" ")[0]
        n=int(e.split(" ")[1])
        i,s=0,0
        
        if d=="R": i,s=0,1
        elif d=="L": i,s=0,-1
        elif d=="U": i,s=1,1
        elif d=="D": i,s=1,-1
              
        for k in range(n):
            h_pos[i]=h_pos[i] + s*1
            t_pos=movement(t_pos, h_pos)

            if not(t_pos[1] in t_map.keys()):
                t_map[t_pos[1]]=[t_pos[0]]
            else:
                if not(t_pos[0] in t_map[t_pos[1]]):
                    t_map[t_pos[1]].append(t_pos[0])
    return sum([ len(d) for d in t_map.values()])
                
p1()