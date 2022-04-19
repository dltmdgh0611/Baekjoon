tri = []
size = int(input())
for _ in range(size):
    tri.append(list(map(int, input().split())))

dp = [[0 for j in range(i+1)]for i in range(size)]

for i in range(1,size):
    for j in range(len(tri[i])):
        dp[i][j] = max(dp[i][j] + dp[i-1][j], dp[i][j] + dp[i-1][j-1])

pass