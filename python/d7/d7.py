f = open("./data/d7/input.txt")
l = [ x for x in ''.join(f.readlines()).strip().split('\n') ]

class Dir:
    def __init__(self, name, parent_dir):
        self.name=name
        self.size=0
        self.sub_dir=[]
        self.parent_dir=parent_dir

    def find_sub_dir(self, name):
        for s in self.sub_dir:
            if s.name==name:
                return s
        return None
    
    def add_sub_dir(self, dir):
        self.sub_dir.append(dir)
    
    def add_size(self, size):
        if self.parent_dir!=None:
            self.parent_dir.add_size(size)
        self.size+=size
        
              
def build_dir():
    i=0
    dir_list=[]
    current_dir=None
    while i<len(l):
        if l[i][:4]=="$ cd":
            if l[i]=="$ cd ..":
                current_dir=current_dir.parent_dir
            else:
                dir_name=l[i].split(" ")[2]
                if current_dir!=None:
                    current_dir=current_dir.find_sub_dir(dir_name)
                else:
                    current_dir=Dir(dir_name, None)
                    dir_list.append(current_dir)
            i+=1

        if l[i]=="$ ls":
            j=i+1
            while j<len(l) and l[j][0]!="$":
                if l[j][0:3]=="dir":
                    dir_name=l[j].split(" ")[1]
                    d=Dir(dir_name, current_dir)
                    current_dir.add_sub_dir(d)
                    dir_list.append(d)
                
                else:
                    current_dir.add_size(int(l[j].split(" ")[0]))
                j+=1
            i=j

    return dir_list

def p1():
    dir_list=build_dir()
    sizes=[ d.size for d in dir_list ]
    low_sizes=[ s for s in sizes if s<=100000 ]
    return sum(low_sizes)
    
def p2():
    dir_list=build_dir()
    dir_list.sort(key=lambda d: d.size)
    total_outermost=dir_list[len(dir_list)-1].size
    unused_space=70000000-total_outermost
    size_to_delete=30000000-unused_space
    s=[ d.size for d in dir_list if d.size>=size_to_delete ][0]
    return s

p1()
p2()