class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def is_self_dividing(num):
            num_str = str(num)
            
            if '0' in num_str:
                return False
            
            for n in num_str:
                if num % int(n) != 0:
                    return False
            
            return True
    
        return [x for x in range(left, right + 1) if is_self_dividing(x)]