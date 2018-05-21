class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A_prime = []
        
        for i, x in enumerate(A):
            A_prime.append(x[::-1])
        
        for i, row in enumerate(A_prime):
            for j, element in enumerate(row):
                if A_prime[i][j] == 0:
                    A_prime[i][j] = 1
                else:
                    A_prime[i][j] = 0
                    
        return A_prime