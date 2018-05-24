from functools import reduce

class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        
        def reduce_ops(a, b):
            return min(a[0], b[0]), min(a[1], b[1])
            
        op1, op2 = tuple(reduce(reduce_ops, ops))
        
        return op1 * op2