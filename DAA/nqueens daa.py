def is_safe(board,row,col,n):
    
    #check row and col
    for i in range(n):
        if board[i][col]==1 or board[row][i]==1:
            return False
    
    
    for i in range(1,n):
        
        if row-i>=0 and col-i>=0:
            if board[row-i][col-i]==1:
                return False
        
        if row-i>=0 and col+i<n:
            if board[row-i][col+i]==1:
                return False
        
        if row+i<n and col-i>=0:
            if board[row+i][col-i]==1:
                return False
            
        
        if row+i<n and col+i<n:
            if board[row+i][col+i]==1:
                return False
    return True

def solve(board,row,n):
    if row==n:
        return True
    
    for col in range(n):
        if board[row][col]==1:
            return solve(board,row+1,n)
        
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            
            if solve(board,row+1,n):
                return True
            
            board[row][col]=0
    return False

def print_board(board):
    for row in board:
        print(*row)
        
n=int(input("Enter value of n :"))
r=int(input("Entert the row to place the queen "))
c=int(input("Entert the col to place the queen "))

board=[[0]*n for i in range(n)]

if n>0 and 1<=r<=n and 1<=c<=n:
    board[r-1][c-1]=1
    
    if solve(board,0,n):
        print("Solution :")
        print_board(board)
        
    else:
        print("Solution does not exits")
else:
    print("invalide position")
        
    
    



    
            
        
            
            
    
            
    
    
            
                
