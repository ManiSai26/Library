graph = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : []
}
visited=[]
queue=[]
def bfs(graph,visited,node):
    visited.append(node)
    queue.append(node)
    while queue:
        src=queue.pop(0)
        print(src)
        for i in graph[src]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
bfs(graph,visited,'A')