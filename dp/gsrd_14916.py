n = int(input())
dp = [99999 for _ in range(n+1)]

if n > 5:
    dp[2] = dp[5] = 1

    for i in range(2,n+1):
        if dp[i-2] != 99999 or dp[i-5] != 99999: 
            dp[i] = min(dp[i-2], dp[i-5]) + 1
            
    if dp[n] != 99999:
        print(dp[n])
    else :
        print(-1)
        
elif n == 1 : print(-1)
elif n == 2 : print(1)
elif n == 3 : print(-1)
elif n == 4 : print(2)
elif n == 5 : print(1)