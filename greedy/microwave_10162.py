time = int(input())
buttons = [300,60,10]
result = [0,0,0]

def solu(t):
    minuscount = 0
    for j in buttons:
        if t/j - int(t/j) != 0:
            minuscount+=1
    if minuscount == 3:
        return [-1]
    for c, i in enumerate(buttons):
        result[c] += t // i
        t = t % i
    return result

for _ in solu(time):
    print(_, end=' ')
