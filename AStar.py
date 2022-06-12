class Node:
    def __init__(self,data,level,fval):
        self.data=data
        self.level=level
        self.fval=fval
    def find(self,puz,x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if(puz[i][j]==x):
                    return (i,j)
    def copy(self,puz):
        res=[]
        for i in range(len(self.data)):
            a=[]
            for j in range(len(self.data)):
                a.append(puz[i][j])
            res.append(a)
        return res
    def shuffle(self,puz,x1,y1,x2,y2):
        if(x2>=0 and y2>=0 and x2<len(self.data) and y2<len(self.data)):
            temp=self.copy(puz)
            t=temp[x1][y1]
            temp[x1][y1]=temp[x2][y2]
            temp[x2][y2]=t
            return temp
        else:
            return None
    def generate_child(self):
        x,y=self.find(self.data,'_')
        sol=[[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
        children=[]
        for i in sol:
            child=self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node=Node(child,self.level+1,0)
                children.append(child_node)
        return children
class Puzzle:
    def __init__(self,size):
        self.n=size
        self.open=[]
        self.closed=[]
    def accept(self):
        puz=[]
        for i in range(self.n):
            puz.append(list(input().split(" ")))
        return puz
    def f(self,start,goal):
        return start.level+self.h(start.data,goal)
    def h(self,start,goal):
        s=0
        for i in range(self.n):
            for j in range(self.n):
                if(start[i][j]!=goal[i][j] and start[i][j]!='_'):
                    s+=1
        return s
    def process(self):
        print("Enter Start state")
        start=self.accept()
        print("Enter Goal State")
        goal=self.accept()
        start=Node(start,0,0)
        start.fval=self.f(start,goal)
        self.open.append(start)
        while True:
            print(" |")
            print(" |")
            print("\\'/")
            cur=self.open[0]
            for i in range(self.n):
                for j in range(self.n):
                    print(cur.data[i][j],end=" ")
                print()
            if(self.h(cur.data,goal)==0):
                break
            else:
                children=cur.generate_child()
                for child in children:
                    child.fval=self.f(child,goal)
                    self.open.append(child)
                self.closed.append(cur)
                del self.open[0]
            self.open.sort(key=lambda x:x.fval)
puzzle=Puzzle(3)
puzzle.process()

