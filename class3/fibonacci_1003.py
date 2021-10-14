length = int(input())
li = []
fibo = [0 for i in range(41)]
fibo[1] = 1

for i in range(2,41):
    fibo[i] = fibo[i-1] + fibo[i-2]

fibo.insert(0,1)

for _ in range(length):
    li.append(int(input()))

for i in li :
    print(fibo[i], fibo[i+1])



