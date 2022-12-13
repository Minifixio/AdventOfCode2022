f = open("./data/d8/input.txt")
l = [ x for x in ''.join(f.readlines()).strip().split('\n') ]

width=len(l[0])
height=len(l)

class Visibility:
    def __init__(self):
        self.right=True
        self.left=True
        self.top=True
        self.bottom=True
    
    def visibility_table(self):
        return (int(self.left), int(self.right), int(self.top), int(self.bottom))
        
visibility_map=[[ Visibility() for i in range(width) ] for j in range(height) ]

def visible_row():
    for i in range(height):
        trees=[ [] for k in range(10) ]
        e=l[i]
        for j in range(width):
            tree_height=int(e[j])
            trees[tree_height].append(j)
            for k in range(0, tree_height+1):
                for ind in trees[k]:
                    if ind!=j:
                        visibility_map[i][ind].right=False
            if sum([ len(trees[i]) for i in range(tree_height, 10) ])-1>0:
                visibility_map[i][j].left=False

def visible_col():
    for i in range(width):
        trees=[ [] for k in range(10) ]
        e=[ x[i] for x in l ]
        for j in range(height):
            tree_height=int(e[j])
            trees[tree_height].append(j)
            for k in range(0, tree_height+1):
                for ind in trees[k]:
                    if ind!=j:
                        visibility_map[ind][i].bottom=False
            if sum([ len(trees[i]) for i in range(tree_height, 10) ])-1>0:
                visibility_map[j][i].top=False

def p1():
    visible_row()
    visible_col()
    valid=[[ 0 if x.visibility_table()==(0,0,0,0) else 1 for x in v ] for v in visibility_map]
    return sum([sum(x) for x in valid])

def p2():
    scenic=[ [(0,0,0,0) for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            tree_height=int(l[i][j])
            right=0
            k=j+1
            while k<width:
                if int(l[i][k])>=tree_height:
                    right+=1
                    break
                right+=1
                k+=1
            left=0
            k=j-1
            while k>=0:
                if int(l[i][k])>=tree_height:
                    left+=1
                    break
                left+=1
                k-=1
            bottom=0
            k=i+1
            while k<height:
                if int(l[k][j])>=tree_height:
                    bottom+=1
                    break
                bottom+=1
                k+=1
            top=0
            k=i-1
            while k>=0:
                if int(l[k][j])>=tree_height:
                    top+=1
                    break
                top+=1    
                k=k-1
            scenic[i][j]=(left,right,top,bottom)
    scenic_score=[ [c[0]*c[1]*c[2]*c[3] for c in s] for s in scenic ] 
    return max([ max(score) for score in scenic_score ])

p1()
p2()