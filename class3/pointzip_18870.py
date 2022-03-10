n = int(input())
li = list(map(int, input().split()))
t = li
tmp = {}
li = list(set(li))
li.sort()
for c, i in enumerate(li):
    tmp[i] = c
for i in t:
    print(tmp[i], end=" ")

