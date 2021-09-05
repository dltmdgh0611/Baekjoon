y,x = input().split()
y,x = int(y),int(x)
chess = []
answer1 = []
answer2 = []
result = []
count = 0
ucount = 0
for i in range(y):
    chess.append(list(input()))

for ay in range(8):
    li1 = []
    li2 = []
    for ax in range(8):
        if ax%2==0:
            if ay%2==0: 
                li1.append('B')
                li2.append('W')
            else : 
                li1.append('W')
                li2.append('B')
        else :
            if ay%2==0: 
                li1.append('W')
                li2.append('B')
            else : 
                li1.append('B')
                li2.append('W')
    answer1.append(li1)
    answer2.append(li2)

for cy in range(y-7):
    for cx in range(x-7):
        for py in range(8):
            for px in range(8):
                gy = cy + py
                gx = cx + px
                if answer1[py][px] != chess[gy][gx] : count = count + 1
                elif answer2[py][px] != chess[gy][gx] : ucount = ucount + 1
        result.append(count)
        result.append(ucount)
        count = 0
        ucount = 0     
print(min(result))
        
