import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
s, e = 1, max(lan)

while s <= e:
    m = (s + e) // 2 
    lines = 0
    for i in lan:
        lines += i // m
        
    if lines >= N: 
        s = m + 1
    else:
        e = m - 1
print(e)