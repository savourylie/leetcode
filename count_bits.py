import math

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result_list = []
        
        for x in range(num + 1):
            if x == 0:
                result_list.append(0)
                continue
            if x == 1:
                result_list.append(1)
                continue
            
            count = 1
            highest_order = int(math.log2(x))
            
            res = x % (2**highest_order)
            count += result_list[res]
            result_list.append(count)
            
        return result_list
        
        
        # return [(lambda x: bin(x)[2:].count('1'))(n) for n in range(num + 1)]