'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

https://leetcode.com/problems/set-matrix-zeroes/description/
'''


def set_zeroes(matrix):
    indexes = []
    seen = set()
    m,n = len(matrix), len(matrix[0])
    RIGHT_WALL, DOWN_WALL, LEFT_WALL, UP_WALL = n,m,-1,-1
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                indexes.append((i,j))
    
    while indexes:
        popped = indexes.pop()
        i,j = popped
        while j < RIGHT_WALL:
            matrix[i][j] = 0
            j += 1
        i,j = popped
        
        while i < DOWN_WALL:
            matrix[i][j] = 0
            i += 1
        i,j = popped
        while j > LEFT_WALL:
            matrix[i][j] = 0
            j -= 1
        i,j = popped
        while i > UP_WALL:
            matrix[i][j] = 0
            i -= 1

    return matrix
    
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_zeroes(matrix))
print(set_zeroes(matrix_2))