from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows =  len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if  (row==0 or col==0 or row==rows-1 or col==cols-1):
                    if grid[row][col]==1:
                        queue.append((row,col))
                        visited[row][col]=1
        while len(queue)!=0:
            i,j = queue.popleft()
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i,new_j = i+x,j+y
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if grid[new_i][new_j]==0:
                    continue
                if grid[new_i][new_j]==1 and visited[new_i][new_j]==1:
                    continue
                queue.append((new_i,new_j))
                visited[new_i][new_j]=1
        count =0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    count+=1
        return count
