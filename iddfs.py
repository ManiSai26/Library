from collections import defaultdict
graph=defaultdict(list)
def addEdge(u,v):
    graph[u].append(v)
def DLS(maxdepth,node,target):
    if(node==target): return True
    if(maxdepth<=0): return False
    for neighbour in graph[node]:
        if(DLS(maxdepth-1,neighbour,target)):
            return True
    return False
def IDDFS(src,target,maxdepth):
    for i in range(maxdepth):
        if(DLS(i,src,target)):
            return i
    return -1
addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(1, 4)
addEdge(2, 5)
addEdge(2, 6)
res=IDDFS(0,6,3)
print(res)
