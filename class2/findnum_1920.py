l1 = int(input())
li1 = sorted(map(int, input().split()))
l2 = int(input())
li2 = map(int, input().split())

result = []

for i in li2:
    start, end = 0, len(li1)-1
    while start <= end:
        middle = (start + end)//2
        if i == li1[middle]:
            result.append(1)
            break
        elif i < li1[middle]: end = middle - 1
        else : start = middle + 1
    if start > end : result.append(0)

for i in result:
    print(i)


