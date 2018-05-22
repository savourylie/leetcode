from math import sqrt, log2

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime_count = 0
        
        # def is_prime(num):
        #     if num not in {2, 3, 5, 7, 11, 13, 17, 19}:
        #         return False
        #     return True
            
        def num_set_bits(num):
            bin_num = bin(num)[2:]
            
            return bin_num.count('1')
        
        def is_prime(num):
            if num < 2:
                return False
            
            if num == 2:
                return True
            
            if num % 2 == 0:
                return False
            
            for x in range(3, int(sqrt(num)) + 2):
                if num % x == 0:
                    return False
            
            return True
        
#         def num_set_bits(num):
#             res = num
#             count = 0
            
#             while res > 0:
#                 highest_digit = int(log2(res))
#                 res = res % 2**highest_digit
#                 count += 1
                
#             return count
        
        for x in range(L, R + 1):
            num = num_set_bits(x)
            if is_prime(num):
                prime_count += 1
                
        return prime_count