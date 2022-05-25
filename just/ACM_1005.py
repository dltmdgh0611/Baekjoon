T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    buildtime = list(map(int, input().split()))
    buildrule = []
    buildingInfo = []
    buildingInfo.append(buildtime[0])
    for i in range(K):
        buildrule.append(list(map(int, input().split())))
    W = int(input())

    buildrule.sort()
    
    for i in range(2,N+1):
        techlist = []
        totaltime = buildtime[i-1]
        tech = []
        for a in buildrule:
            if a[1] == i:
                tech.append(a[0])
        for b in tech:
            techlist.append(buildingInfo[b-1])
        totaltime+=max(techlist)
        buildingInfo.append(totaltime)
    print(buildingInfo[W-1])



