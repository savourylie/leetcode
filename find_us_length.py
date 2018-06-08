class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) > len(b):
            return len(a)
        elif len(a) < len(b):
            return len(b)
        
        if a == b:
            return -1
            
        
        i = len(b)
        
        while i > 0:
            if b[:i] not in a:
                return len(b[:i])
            i -= 1
            
        return -1