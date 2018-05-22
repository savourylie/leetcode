class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        max_size = 0
        island_count = 0

        def check_and_change_neighbors(i, j):
            size = 0

            if grid[i][j] != 1:
                return size

            neighbors = [(i + x, j) for x in {-1, 1} if 0 <= i + x < M] \
            + [(i, j + x) for x in {-1, 1} if 0 <= j + x < N]

            grid[i][j] = '*'
            size += 1

            for u, v in neighbors:
                 size += check_and_change_neighbors(u, v)

            return size

        for i in range(M):
            for j in range(N):
                temp_size = check_and_change_neighbors(i, j)
                max_size = max(max_size, temp_size)

        return max_size