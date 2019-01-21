class Solution(object):
    def __init__(self):
        self.count = 0

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                neighbors = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]

                for u, v in neighbors:
                    if grid[u][v] == 0:
                        grid[u][v] = 1

                        self.uniquePathsIII(grid)

                    elif grid[u][v] == 2:
                        if self.legal_path(grid):
                            self.count += 1


                    else:


    def legal_path(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    return False

        return True

