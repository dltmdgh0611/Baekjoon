N, M = map(int, input().split())
li = [[1]]
for i in range(N):
    li2 = []
    for j in range(i):
        num = 0
        if j == 0 : li2.append(1)
        elif j == i: li2. append(1)
        else:
            try : num += li[i-1][j-1]
            except : pass
            try : num += li[i-1][j]
            except : pass
            li2.append(num)
    li.append(li2)
