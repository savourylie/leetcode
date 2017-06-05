class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_copy = n
        i = 0
        
        while n_copy > 0:
            n_copy -= (i + 1) * 9 * 10**i
            i += 1
        
        nth_term = i - 1
        
        if n_copy == 0:
            return 9
            
        else:
            n_copy = n
            
            for j in range(nth_term):
                n_copy -= (j + 1) * 9 * 10**j
                
            quo, res = divmod(n_copy, i)
            
            if res == 0:
                return int(str(quo + 10**nth_term - 1)[-1])
                
            else:
                return int(str(quo + 10**nth_term - 1 + 1)[res - 1])
            
        