class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        len_arr = len(S)
        
        start = 0
        prev = S[0]
        result_list = []
        
        for i, x in enumerate(S):
            if x != prev:
                end = i - 1
                
                if end - start + 1 > 2 :
                    result_list.append([start, end])    
                    
                start = i
                prev = x
        
        
        if len_arr - 1 - start + 1 > 2 :
            result_list.append([start, len_arr - 1]) 
            
        return result_list