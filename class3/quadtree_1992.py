n = int(input())
qt = [list(map(int, input())) for _ in range(n)]

def search(x,y,n):
    check = qt[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if qt[i][j] != check: 
                check = -1
                break
    
    if check == -1:
        n //= 2
        print("(", end='')
        search(x,y,n)
        search(x,y+n,n)
        search(x+n,y,n)
        search(x+n,y+n,n)
        print(")", end='')
    elif check == 1:
        print(1, end='')
    else :
        print(0, end='')

search(0,0,n)


