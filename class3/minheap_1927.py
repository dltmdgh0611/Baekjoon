import heapq
n = int(input())
h = []
result = []
for _ in range(n):
    i = int(input())
    if i == 0 :
        if len(h) == 0: result.append(0)
        else :
            result.append(heapq.heappop(h))
            
    else : 
        heapq.heappush(h,i)

for i in result:
    print(i)