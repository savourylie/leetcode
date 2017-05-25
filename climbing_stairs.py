import math

class Solution(object):
    # combinatorics approach
    def combi_climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        
        if n % 2 != 0:
            start = int(n/2) + 1
            for x in range(start, n + 1):
                result += self.nCr(x, 1 + (x - start)*2)
            
        else:
            start = n/2
            for x in range(start, n + 1):
                result += self.nCr(x, (x - start)*2)
            
        return result
            
        
    def nCr(self, n, r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)
        
    # dynamic programming approach
    def climbStairs(self, n):
        
        ways_of_climbing_stairs = [1, 1]
        
        while len(ways_of_climbing_stairs) < n + 1:
            ways_of_climbing_stairs.append(ways_of_climbing_stairs[-2] + ways_of_climbing_stairs[-1])
            
        return ways_of_climbing_stairs[-1]