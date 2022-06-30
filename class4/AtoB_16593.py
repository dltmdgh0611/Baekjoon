A, B = list(map(int, input().split()))
count = 1
while A != B:
    count+=1
    temp = B
    if B%10 == 1:
        B//=10
    elif B % 2 == 0:
        B //= 2
    if temp == B :
        count = -1
        break

print(count)