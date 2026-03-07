class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visit, prev):
            if (r < 0 or c < 0 or r >= m or c >= n or
                (r, c) in visit or heights[r][c] < prev):
                return
            
            visit.add((r, c))
            
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])
        
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])
        
        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        
        return res