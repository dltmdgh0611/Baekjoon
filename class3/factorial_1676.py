n = int(input())
sum = 1
value = 0
for i in range(1,n+1):
    sum *= i
sum = list(str(sum))
sum.reverse()
for s in sum:
    if s == '0':
        value+=1
    else : break
print(value)