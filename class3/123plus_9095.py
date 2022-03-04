n = int(input())
ans = []
li = [1,2,4]
for _ in range(n):
    ans.append(int(input()))

for i in range(max(ans)):
    if i > 2:
        li.append(li[i-1]+li[i-2]+li[i-3])

for i in ans:
    print(li[i-1])

