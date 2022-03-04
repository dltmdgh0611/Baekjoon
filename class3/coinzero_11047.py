N, price = map(int, input().split())
coin = []
cs = 0
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
for c in coin:
    if price // c == 0:
        pass
    else :
        cs += price // c
        price %= c
        
print(cs)