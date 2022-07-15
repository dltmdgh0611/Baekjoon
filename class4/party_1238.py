import heapq
INF = 1e8
student, road, partyspace = map(int, input().split())
graph = [[] for _ in range(road+1)]
distance = [INF] * (road+1)
for _ in range(road):
    s,e,w = map(int, input().split())
    graph[s].append((e,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist+i[i] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

                