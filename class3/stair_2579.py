stair = []
dp = [[0 for i in range(3)]for x in range(302)]
n = int(input())
for _ in range(n):
    stair.append(int(input()))


dp[0][0] = dp[0][1] = 0
if n != 0: dp[1][1] = dp[1][2] = stair[0]

for i in range(2, n+1):
    dp[i][2] = dp[i-1][1] + stair[i-1]
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stair[i-1]

print(max(dp[n][1],dp[n][2]))
