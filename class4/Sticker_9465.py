N = int(input())
for _ in range(N):
    row = int(input())
    table = []
    for i in range(2):
        table.append(list(map(int, input().split())))
    try:
        table[0][1] += table[1][0]
        table[1][1] += table[0][0]
    except: pass
    for i in range(2, row):
        table[0][i] += max(table[1][i-1], table[1][i-2])
        table[1][i] += max(table[0][i-1], table[0][i-2])
    print(max(map(max, table)))
pass

