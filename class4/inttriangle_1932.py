tri = []
size = int(input())
for _ in range(size):
    tri.append(list(map(int, input().split())))

dp = tri

for i in range(1,size):
    for j in range(len(tri[i])):
        if j==0: dp[i][j] += dp[i-1][0]
        elif j==len(tri[i])-1: dp[i][j] += dp[i-1][len(tri[i-1])-1]
        else : dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[len(dp)-1]))