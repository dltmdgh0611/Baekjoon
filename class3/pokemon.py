import sys

input = sys.stdin.readline

N, M = map(int, input().split())

di = {}

for i in range(1, N + 1):
    a = input().rstrip()
    di[i] = a
    di[a] = i

for i in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(di[int(q)])
    else:
        print(di[q])