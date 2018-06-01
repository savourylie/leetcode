class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_idx_dict = {}
        
        for i, x in enumerate(S):
            last_idx_dict[x] = max(i, last_idx_dict.get(x, i))
            
        result_list = []
        
        start, last = 0, 0
        
        for i, x in enumerate(S):
            last = max(last_idx_dict[x], last)
            
            if i == last:
                result_list.append(last - start + 1)
                start = i + 1
                
        return result_list