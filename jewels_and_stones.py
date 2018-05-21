class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_set = set(J)
        counter = 0
        
        for i, x in enumerate(S):
            if x in jewel_set:
                counter += 1
                
        return counter