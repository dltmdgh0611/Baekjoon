N = int(input())
paper = []
for _ in range(N):
    paper.append(input().split())

result = [0,0,0]

def Divnine(paper, k):
    first = paper[0][0]
    wak = True
    for p in paper:
        for _ in p:
            if first != _ :
                wak = False
                break

    if wak:
        if first == '-1': return 0
        elif first == '0': return 1
        elif first == '1' : return 2
    
    k = int(k/3)
    for i in range(3):
        for j in range(3):
            slicePaper = [row[j*k:j*k+k] for row in paper[i*k:i*k+k]]
            temp = Divnine(slicePaper,k)
            if temp is not None :
                result[temp] += 1

temp = Divnine(paper, N)
if temp is not None:
    result[temp] += 1

for i in result:
    print(i)
