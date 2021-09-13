number = int(input())
tmp = number
result = []
while True:
    if tmp == 0:
        break
    if tmp < number - 100:
        break
    div = [int(a) for a in str(tmp)]
    if sum(div) + tmp == number:
        result.append(tmp)
    tmp-=1

if not result : print(0)
else : print(min(result))

