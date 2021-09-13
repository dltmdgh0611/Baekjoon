dummy = input()
li = map(int, input().split())
count = 0
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for i in li:
    if i in primes:
        count += 1

print(count)