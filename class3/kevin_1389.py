from collections import deque
N,M = map(int, input().split())
graph = {}
result = [0 for i in range(N)]
s = [0 for i in range(N)]

def BFS(graph, root):
    visited = []
    predecessor = [0] * N
    queue = deque([root])

    visited.append(root)

    while queue:
        cur = queue.popleft()
        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.append(neighbor)
                predecessor[neighbor - 1] = cur
                queue.append(neighbor)
    return predecessor

def back(pre, end):
    r = 0
    pointer = pre[end-1]
    while True:
        if pointer == 0 : return r
        r += 1
        pointer = pre[pointer-1]


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
    

for i in range(1,N+1):
    result = BFS(graph, i)
    for j in range(1,N+1):
        if i!=j:
            s[j-1] += back(result, j)

l = []
for c, i in enumerate(s):
    if i == min(s):
        l.append(c+1)

print(min(l))

    