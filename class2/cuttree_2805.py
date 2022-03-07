n,m = map(int, input().split())
li = list(map(int, input().split()))
start, end = 1, max(li)
while start <= end:
    cutline = (start+end)//2
    s = 0
    for i in li :
        if i > cutline:
            s += (i - cutline)

    if s >= m:
        start = cutline + 1
    else :
        end = cutline - 1

print(end)