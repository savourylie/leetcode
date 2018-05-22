class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if matrix is None:
            return True
        if len(matrix) == 0 or len(matrix) == 1:
            return True
        
        M = len(matrix)
        N = len(matrix[0])
        diag_num = M + N - 1
        
        realigned_list = [[None] * (diag_num - N - i) + row + [None] * i for i, row in enumerate(matrix)]
        diag_list = list(zip(*realigned_list))
        
        for x in [[element for element in row if element is not None] for row in diag_list]:
            if len(set(x)) != 1:
                return False
            
        return True