n = int(input())
li = []
dp = [[0 for i in range(3)]for x in range(n+1)]
for _ in range(n):
    li.append(int(input()))

dp[0][0] = dp[0][1] = 0
if n != 0: dp[1][1] = dp[1][2] = li[0]

for i in range(2, n+1):
    dp[i][2] = dp[i-1][1] + li[i-1]
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + li[i-1]

print(max(map(max, dp)))