N = int(input())
li = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, li[i - (j**2)])
        j += 1

    li.append(min_value + 1)
print(li[N])