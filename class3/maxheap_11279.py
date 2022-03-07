import heapq, sys
n = int(sys.stdin.readline())
li = []

for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        heapq.heappush(li, -i)
    else:
        if len(li) == 0:
            print(0)
        else:
            print(-heapq.heappop(li))
            
