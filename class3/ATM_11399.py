n = int(input())
li = list(map(int, input().split()))
li.sort()
result = 0
for i in range(1,n+1):
    result += sum(li[:i])

print(result)

