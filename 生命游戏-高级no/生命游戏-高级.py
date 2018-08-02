


def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    m = len(board)
    if m==0:
    	return []
    n=len(board[0])
    my = [[-1 for j in range(n)] for i in range(m)]
    for i in range(m):
    	for j in range(n):
    		if i == 0:
    			if j==0:
    				sums = board[i+1][j]+board[i+1][j+1]+board[i][j+1]
    			elif j==n-1:
    				sums = board[i][j-1]+board[i+1][j-1]+board[i+1][j]
    			else:
    				sums = board[i+1][j]+board[i+1][j+1]+board[i][j+1] +  board[i][j-1]+board[i+1][j-1]
    		elif i == m-1:
    			if j==0:
    				sums = board[i-1][j]+board[i-1][j+1]+board[i][j+1]
    			elif j==n-1:
    				sums = board[i][j-1]+board[i-1][j]+board[i-1][j-1]
    			else:
    				sums = board[i][j-1]+board[i-1][j]+board[i-1][j-1]+board[i-1][j+1]+board[i][j+1]
    		elif j == 0:
    			sums = board[i][j+1] +board[i-1][j+1]+board[i+1][j+1]+board[i-1][j]+board[i+1][j]
    		elif j == n-1:
    			sums = board[i][j-1] + board[i-1][j-1]+board[i+1][j-1]+board[i-1][j]+board[i+1][j]
    		else:
    			sums = board[i-1][j-1]+ board[i-1][j]+ board[i-1][j+1]+board[i+1][j]+board[i+1][j-1]+board[i+1][j+1]+board[i][j-1]+board[i][j+1]

    		if sums<2 or sums>3:
    			my[i][j] = 0
    		elif sums==2:
    			my[i][j] = 1
    		else:
    			my[i][j] = board[i][j]

    board[:] = my