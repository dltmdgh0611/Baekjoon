from collections import deque
N,M = map(int, input().split())
graph = {}
result = [0 for i in range(M)]

def BFS(graph, root, goal):
    visited = []
    depthlist = [0] * M
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            depthlist[n-1] = depthlist[root] + 1
            if goal == n: return depthlist[n]
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return -1

for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    elif a not in graph[b]:
        graph[b].append(a)
    

for i in range(1,M+1):
    for j in range(1,M+1):
        if i != j:
            result[i-1] += BFS(graph, i, j)


pass
    
