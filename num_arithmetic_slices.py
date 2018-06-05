class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        n = len(A)
        
        if n < 3:
            return 0
        
        for i in range(n-3+1):
            diff = None
            for j in range(i+1, n):
                if j == i + 1:
                    diff = A[j] - A[i]
                    continue
                    
                else:
                    if A[j] - A[j-1] != diff:
                        break
                    else:
                        count += 1
        
        return count
                    
                    
                    