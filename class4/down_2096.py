import sys
f = sys.stdin.readline
n = int(f())
li = []
k = 0
maxdp = [[0 for _ in range(3)] for _ in range(2)]
mindp = [[0 for _ in range(3)] for _ in range(2)]

for i in range(n):
    x1, x2, x3 = map(int, f().split())
    maxdp[k][0] = max(maxdp[1-k][0], maxdp[1-k][1]) + x1
    maxdp[k][1] = max(maxdp[1-k][0], maxdp[1-k][1], maxdp[1-k][2]) + x2
    maxdp[k][2] = max(maxdp[1-k][1], maxdp[1-k][2]) + x3

    mindp[k][0] = min(mindp[1-k][0], mindp[1-k][1]) + x1
    mindp[k][1] = min(mindp[1-k][0], mindp[1-k][1], mindp[1-k][2]) + x2
    mindp[k][2] = min(mindp[1-k][1], mindp[1-k][2]) + x3
    k = 1-k


print(max(maxdp[1-k][0],maxdp[1-k][1],maxdp[1-k][2]), min(mindp[1-k][0],mindp[1-k][1],mindp[1-k][2]))

