class Solution:
    def dfs(self,r,c,grid,visited,rows,cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return 
        if visited[r][c] == 1 :
            return 
        if grid[r][c] == "0" : 
            return 
        
        visited[r][c] = 1
        self.dfs(r-1,c,grid,visited,rows,cols)
        self.dfs(r+1,c,grid,visited,rows,cols)
        self.dfs(r,c-1,grid,visited,rows,cols)
        self.dfs(r,c+1,grid,visited,rows,cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        num_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    num_of_islands += 1
                    self.dfs(r,c,grid,visited,rows,cols)
        return num_of_islands
