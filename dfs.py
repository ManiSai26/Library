graph = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : []
}
def dfs(visited,graph,src):
    if src not in visited:
        print(src)
        visited.append(src)
        for neighbour in graph[src]:
            dfs(visited,graph,neighbour)
dfs([],graph,'A')

