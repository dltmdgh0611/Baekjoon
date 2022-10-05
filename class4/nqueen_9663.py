count = 0
n = int(input())
board = [0 for x in range(15)]

def promising(cdx):
    for i in range(cdx):
        if board[cdx] == board[i] or cdx - i == abs(board[cdx] - board[i]):
            return 0

    return 1

def nqueen(cdx):
    global count 
    if cdx==n:
        count+=1
        return

    for i in range(n):
        board[cdx] = i
        if(promising(cdx)):
            nqueen(cdx + 1)

nqueen(0)
print(count)
