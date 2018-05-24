class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
            
        def skyline(grid, view='top'):
            M = len(grid)
            N = len(grid[0])
            
            top = [max([grid[i][j] for i in range(M)]) for j in range(N)]
            left = [max([grid[i][j] for j in range(N)]) for i in range(M)]
            
            return top if view == 'top' else left
        
        top, left = skyline(grid, view='top'), skyline(grid, view='left')
        
        incremental = 0
        
        for i in range(M):
            for j in range(N):
                incremental += min(top[j], left[i]) - grid[i][j]
        
        return incremental