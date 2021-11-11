import sys
sys.setrecursionlimit(10**6)

case = int(input())
farm = []
global count

def search(x, y, n, m):
    global count
    if y+1 < M:
        if farm[y+1][x] == 1: 
            farm[y+1][x] = 2
            count -= 1
            search(x, y+1, n, m)
    if y-1 >= 0:
        if farm[y-1][x] == 1: 
            farm[y-1][x] = 2
            count -= 1
            search(x, y-1, n, m)
    if x+1 < N:
        if farm[y][x+1] == 1 :
            farm[y][x+1] = 2
            count -= 1
            search(x+1, y, n, m)
    if x-1 >= 0:
        if farm[y][x-1] == 1 : 
            farm[y][x-1] = 2
            count -= 1
            search(x-1, y, n, m)


for _ in range(case):
    N, M, C = map(int, input().split())
    count = C
    farm = [[0 for i in range(N)] for j in range(M)]
    for __ in range(C):
        x, y = map(int, input().split())
        farm[y][x] = 1
    for y in range(M):
        for x in range(N):
            if farm[y][x] == 2 : continue
            elif farm[y][x] == 1 :
                farm[y][x] = 2
                search(x,y,N,M)
            else : continue
    print(count)

