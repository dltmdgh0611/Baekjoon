length = int(input())

for _ in range(length):
    count = 0
    li = []
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    for c, i in enumerate(q):
        if c == M : li.append((i, 1))
        else : li.append((i, 0))

    while len(li) > 0:
        delete = True
        for j in li:
            if j[0] > li[0][0]:
                li.append(li[0])
                del li[0]
                delete = False
                break
        if delete :
            count += 1
            if li[0][1] == 1:
                break
            del li[0]
    print(count)
            
            
            
        
        
