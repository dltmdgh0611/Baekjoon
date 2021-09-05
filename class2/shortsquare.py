x,y,w,h = input().split()
x,y,w,h = int(x), int(y), int(w), int(h)
li = []
li.append(x)
li.append(y)
li.append(abs(x-w))
li.append(abs(y-h))
print(min(li))