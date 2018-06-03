class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        M, N = len(board), len(board[0])
        count = 0
        
        def check_and_mark_neighbors(i, j):
            if board[i][j] != 'X':
                return 0
            
            else:
                board[i][j] = 'B'
                neighbors = [(i + x, j) for x in {-1, 1} if 0 <= i + x < M] + [(i, j + x) for x in {-1, 1} if 0 <= j + x < N]
                
                for u, v in neighbors:
                    _ = check_and_mark_neighbors(u, v)
                    
            return 1
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'X':
                    count += check_and_mark_neighbors(i, j)
                    
        return count
                
            