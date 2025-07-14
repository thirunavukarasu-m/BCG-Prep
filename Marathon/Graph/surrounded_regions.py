'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''


class Solution:
    def solve(self, board):
        
        m,n = len(board), len(board[0])
        if m == 1 and n == 1:
            return
        
        def dfs(i,j):
            if i < 1  or i == m - 1 or j < 1 or j == n - 1 or board[i][j] == 'X' or (board[i-1][j] == 'O' and board[i+1][j] == 'O' and board[i][j + 1] == 'O' and board[i][j - 1] == 'O'):
                return
          
            board[i][j] = "X"
            dfs(i,j + 1)
            dfs(i,j - 1)
            dfs(i + 1,j)
            dfs(i - 1,j)
            
            
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        return board
        
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
s = Solution()
print(s.solve(board))