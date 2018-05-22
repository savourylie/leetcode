class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return True
        
        bin_n = bin(n)[2:]
        
        if len(bin_n) == 1:
            return True
        
        prev_digit = bin_n[0]
        
        for digit in bin_n[1:]:
            if not bool(int(prev_digit) ^ int(digit)):
                return False
            prev_digit = digit
        
        return True