N=4
board=[['-']*N for _ in range(N)]
def issafe(board,x,y):
    for i in range(N):
        if(x!=i and board[i][y]=='Q'):
            return False
        if(y!=i and board[x][i]=='Q'):
            return False
    i=x-1
    j=y-1
    while(i>=0 and j>=0):
        if(board[i][j]=='Q'):
            return False
        i-=1
        j-=1
    i=x+1
    j=y+1
    while(i<N and j<N):
        if(board[i][j]=='Q'):
            return False
        i+=1
        j+=1
    i=x-1
    j=y+1
    while(i>=0 and j<N):
        if(board[i][j]=='Q'):
            return False
        i-=1
        j+=1
    i=x+1
    j=y-1
    while(i<N and j>=0):
        if(board[i][j]=='Q'):
            return False
        i+=1
        j-=1
    return True
def printsol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()
    print()
def solve(row,board):
    if(row==N):
        printsol(board)
        return
    for i in range(N):
        if(issafe(board,row,i)):
            board[row][i]='Q'
            solve(row+1,board)
            board[row][i]='-'
solve(0,board)
