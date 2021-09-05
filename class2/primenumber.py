min, max = input().split()
min, max = int(min), int(max)

n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for k in primes:
    if k <= max and k >= min:
        print(k)