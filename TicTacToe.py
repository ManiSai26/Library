player,opponent='x','o'
def evaluate(board):
    for row in range(3):
        if(board[row][0]==board[row][1] and board[row][1]==board[row][2]):
            if(board[row][0]==player):
                return 10
            else:
                return -10
    for column in range(3):
        if(board[0][column]==board[1][column] and board[1][column]==board[2][column]):
            if(board[0][column]==player):
                return 10
            else:
                return -10
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        if(board[0][0]==player):
                return 10
        else:
            return -10
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        if(board[0][2]==player):
                return 10
        else:
            return -10
    return 0
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='_'):
                return True
    return False
def minmax(board,depth,isMax):
    res=evaluate(board)
    if(res==10):
        return res
    if(res==-10):
        return res
    if(isMovesLeft(board)==False):
        return 0
    if(isMax):
        best=-1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j]=player
                    val=minmax(board,depth+1,False)
                    board[i][j]='_'
                    best=max(best,val)
        return best
    else:
        best=1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j]=opponent
                    val=minmax(board,depth+1,True)
                    board[i][j]='_'
                    best=min(best,val)
        return best
def findBestMove(board):
    bestval=-1000
    bestMove=(-1,-1)
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='_'):
                board[i][j]=player
                val=minmax(board,0,False)
                board[i][j]='_'
                if(val>bestval):
                    bestval=val
                    bestMove=(i,j)
    return bestMove

board = [
    [ 'x', 'o', 'x' ],
    [ 'o', 'o', 'x' ],
    [ '_', '_', '_' ]
] 
bestMove = findBestMove(board)
 
print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])