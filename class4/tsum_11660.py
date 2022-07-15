from sys import stdin

N, M = map(int, stdin.readline().split())
li = [[0] * (N + 1)]
for i in range(N):
    nums = [0] + [int(x) for x in stdin.readline().split()]
    li.append(nums)

for i in range(1, N + 1):
    for j in range(1, N):
        li[i][j + 1] += li[i][j]

for j in range(1, N + 1):
    for i in range(1, N):
        li[i + 1][j] += li[i][j]

for j in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(li[x2][y2] - li[x1 - 1][y2] - li[x2][y1 - 1] + li[x1 - 1][y1 - 1])
