num = int(input())
depth = 1
p = 1
while True:
    if num <= p:
        break
    depth += 1
    if depth > 1:
        p += depth*6 - 6
print(depth)