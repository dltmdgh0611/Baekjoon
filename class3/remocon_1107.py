channel = int(input())
d = int(input())
breakdown = []
if d > 0:
    breakdown = list(input().split())
current = 100

mincount = abs(current - channel)

for c in range(1000000):
    for i in range(len(str(c))):
        if str(c)[i] in breakdown:
            break
        elif len(str(c)) - 1 == i:
            mincount = min(mincount, abs(c - channel) + len(str(c)))

print(mincount)