'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

https://leetcode.com/problems/spiral-matrix/description/
'''


def spiral_matrix(matrix):
    m,n = len(matrix), len(matrix[0])
    ans = []
    i,j = 0,0
    RIGHT, DOWN, LEFT, UP = 0,1,2,3
    RIGHT_WALL, DOWN_WALL, LEFT_WALL, UP_WALL = n,m,-1,0
    direction = RIGHT
    
    while len(ans) != m * n:
        if direction == RIGHT:
            while j < RIGHT_WALL:
                ans.append(matrix[i][j])
                j += 1
            i,j =  i + 1, j - 1 # i + 1 goes down and j is already out of bounds so we need to reset. so j - 1
            RIGHT_WALL -= 1 # need to update the walls.
            direction = DOWN
        
        elif direction == DOWN:
            while i < DOWN_WALL:
                ans.append(matrix[i][j])
                i += 1
            i,j = i - 1, j - 1 # i goes out of bounds, j needs to go left now.
            DOWN_WALL -= 1
            direction = LEFT
        
        elif direction == LEFT:
            while j > LEFT_WALL:
                ans.append(matrix[i][j])
                j -= 1
            
            i,j = i - 1, j + 1 # j out of bounds and i needs to go up
            LEFT_WALL += 1
            direction = UP
        
        else:
            while i  > UP_WALL:
                ans.append(matrix[i][j])
                i -= 1
            i,j = i + 1, j + 1 # i out of bounds and j needs to go right
            UP_WALL += 1
            direction = RIGHT
    
    return ans
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))