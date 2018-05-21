class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        char_indices = [i for i, char in enumerate(S) if char == C]
        result_list = [min([abs(i - idx) for idx in char_indices]) for i, x in enumerate(S)]
            
        return result_list