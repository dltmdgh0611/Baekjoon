
T = int(input())

def xmax(rule, tech, time):
    li = []
    if len(rule[tech]) == 0:
        return time[tech-1]
    else :
        for i in rule[tech]:
            xmax(rule, i, time)
            li.append(time[i-1])
        time[tech-1] += max(li)
        rule[tech] = []
    return time[tech-1]
            
    

for _ in range(T):
    N, K = map(int, input().split())
    buildtime = list(map(int, input().split()))
    buildrule = {}
    buildingInfo = []
    buildingInfo.append(buildtime[0])
    for i in range(1,N+1):
        buildrule[i] = []
    for i in range(K):
        buildli = list(map(int, input().split()))
        buildrule[buildli[1]].append(buildli[0])
    W = int(input())
    
    print(xmax(buildrule, W ,buildtime))



