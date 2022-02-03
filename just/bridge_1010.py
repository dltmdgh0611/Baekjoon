import math
n = int(input())
for _ in range(n):
    i,j = map(int, input().split())
    print(math.factorial(j) // (math.factorial(j-i) * math.factorial(i)))
