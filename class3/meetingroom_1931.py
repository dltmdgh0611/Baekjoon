a = int(input())
lst = []
last = 0
count = 0

for _ in range(a):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1], x[0]))

for i in lst:
    if i[0] >= last:
        last = i[1]
        count+=1

print(count)
