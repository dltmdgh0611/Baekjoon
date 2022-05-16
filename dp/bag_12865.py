N, K = map(int, input().split())
li = [[0,0]]
dp = [[0]*(K+1) for i in range(N+1)]
for _ in range(N):
    li.append(list(map(int, input().split())))

li.sort(key=lambda x:x[0])

for i in range(N+1):
    for j in range(K+1):
        weight = li[i][0]
        value = li[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else : 
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)

print(dp[N][K])

