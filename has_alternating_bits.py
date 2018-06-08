from math import log2

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n == 1 or n == 2:
            return True
        
        if n == 3:
            return False
        
        highest_digit = int(log2(n))
        res = n
        
        while res > 0 and highest_digit > 0:
            if highest_digit == 2:
                if res == 5:
                    return True
                else:
                    return False
                
            if highest_digit == 3:
                if res == 10:
                    return True
                else:
                    return False
        
            _, res = divmod(res, 2**highest_digit)
            
            highest_digit -= 2
            
            if res > 2**(highest_digit + 1):
                return False
            elif res < 2**(highest_digit):
                return False
            else:
                continue
            
        return True