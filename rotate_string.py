class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
                
        if B in A * 2 and A in B * 2:
            return True
        
        else:
            return False