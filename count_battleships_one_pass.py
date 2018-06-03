class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        M, N = len(board), len(board[0])
        coord_set = set()
        count = 0
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'X':
                    neighbors = [(i, j + x) for x in {1, -1} if 0 <= j + x < N] + [(i + x, j) for x in {1, -1} if 0 <= i + x < M]
                    coord_set.add((i, j))
                    
                    for x in neighbors:
                        if x in coord_set:
                            break
                    else:
                        count += 1
                    
        return count