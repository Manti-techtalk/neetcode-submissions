class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row , col = len(grid),len(grid[0])

        print(row,col)
        seen = set()
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in seen or grid[r][c] == 0:
                return 0
            
            #add to visitd
            seen.add((r,c))

            # now go dow,up,left,right
            area = 1

            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            area+=dfs(r-1,c)
            area+=dfs(r+1,c)


            return area

        self.mxA = 0
        for r in range(row):
            for c in range(col):
                if (r,c) not in seen and grid[r][c] == 1:
                    self.mxA = max(self.mxA,dfs(r,c))

        return self.mxA

