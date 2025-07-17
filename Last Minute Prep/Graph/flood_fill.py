class Solution:
    
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image

        const = image[sr][sc]
        m,n = len(image), len(image[0])


        def dfs(i,j):
            if i < 0 or i >=m or j < 0 or j >= n or image[i][j] == color or image[i][j] != const:
                return
            
            image[i][j] = color
            dfs(i,j + 1)
            dfs(i,j - 1)
            dfs(i + 1,j)
            dfs(i - 1,j)

        
        dfs(sr, sc)
        return image