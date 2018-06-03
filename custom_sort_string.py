class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = ''
        result_not_in_S = ''.join([x for x in T if x not in S])
            
        for x in S:
            for y in T:
                if y == x:
                    result += x
                            
        return result + result_not_in_S