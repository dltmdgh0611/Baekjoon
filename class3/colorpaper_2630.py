n = int(input())
qt = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0,0
def search(x,y,n):
    global blue, white
    check = qt[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if qt[i][j] != check: 
                check = -1
                break

    if check == -1:
        n //= 2
        search(x,y,n)
        search(x,y+n,n)
        search(x+n,y,n)
        search(x+n,y+n,n)
    elif check == 1:
        blue += 1
    elif check == 0:
        white += 1

search(0,0,n)
print(white)
print(blue)