class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        rotate_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', 
                      '8': '8', '9': '6'}
        
        good_count = 0
        
        for n in range(1, N + 1):
            str_n = str(n)
                
            result_n = ''
            valid = True
            
            for digit in str_n:    
                if digit not in rotate_map:
                    valid = False
                    break

                else:
                    result_n += rotate_map[digit]

            if result_n != str_n and valid:
                good_count += 1
                
        return good_count