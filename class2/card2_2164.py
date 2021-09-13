from collections import deque
length = int(input())
li = deque([i for i in range(1,length+1)])

while True:
    if len(li) > 1:
        li.popleft()
    else : break
    if len(li) > 1:
        li.append(li[0])
        li.popleft()
    else : break
print(li[0])
    
    