class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col = len(grid),len(grid[0])
        print(row,col)

        visited = set()
        
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0" or (r,c) in visited:
                return

            #now mark as seen
            visited.add((r,c))

            #now go down,up,left,right
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        self.count = 0
        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and grid[r][c] == '1':
                    self.count +=1
                    dfs(r,c)
        return self.count
        




