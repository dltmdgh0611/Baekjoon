length = int(input())
stack = []
result = []
count = 0
available = True

for _ in range(length):
    n = int(input())

    while count < n:
        count += 1
        stack.append(count)
        result.append('+')


    if stack[-1] == n:
        stack.pop()
        result.append('-')
    else :
        available = False
        break

if available : 
    for i in result:
        print(i)
else : print("NO")
    
