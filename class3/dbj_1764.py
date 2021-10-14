listen, see = map(int, input().split())
lili = []
seeli = []
dbj = []
for _ in range(listen):
    lili.append(input())
for _ in range(see):
    seeli.append(input())
dbj = list(set(lili)&set(seeli))
dbj.sort()
print(len(dbj))
for d in dbj:
    print(d)
