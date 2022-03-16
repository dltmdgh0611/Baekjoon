rgb = []
dp = [[0 for i in range(3)]for x in range(1002)]
n = int(input())
for _ in range(n):
    rgb.append(list(map(int, input().split())))

dp[0] = rgb[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb[i][2]

print(min(dp[n-1]))
