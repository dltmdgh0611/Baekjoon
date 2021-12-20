from collections import deque
visit = []
queue = deque([])
N = int(input())
result = 0

def avail(n):
    if n < 0 or n > 100000 or n in visit :
        return False
    return True

def BFS(root):
    while queue:
        data = queue[0][0]
        depth = queue[0][1]
        queue.popleft()

        if data == N : 
            return depth

        if avail(data + 1):
            visit.append(data-1)
            queue.append([data-1,depth+1])
        if avail(data + 2):
            visit.append(data+1)
            queue.append([data+1,depth+1])