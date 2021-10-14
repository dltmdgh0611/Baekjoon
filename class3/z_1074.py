N, y, x = map(int, input().split())
answer = 0
wm = hm = (2**N) / 2

x = x + 1
y = y + 1
while N:
    if x <= wm and y <= hm:
        #1
        wm = wm - (2**(N - 1)) / 2
        hm = hm - (2**(N - 1)) / 2
        pass
    elif x > wm and y <= hm:
        answer = answer + (2**((N-1)*2)) * 1
        wm = wm + (2**(N - 1)) / 2
        hm = hm - (2**(N - 1)) / 2
        #23 
        pass
    elif x <= wm and y > hm:
        answer = answer + (2**((N-1)*2)) * 2
        wm = wm - (2**(N - 1)) / 2
        hm = hm + (2**(N - 1)) / 2
        #3
        pass
    elif x > wm and y > hm:
        answer = answer + (2**((N-1)*2)) * 3
        wm = wm + (2**(N - 1)) / 2
        hm = hm + (2**(N - 1)) / 2
        #4
        pass
    N-=1
print(answer)
    
