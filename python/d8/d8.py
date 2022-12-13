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
        
p1()