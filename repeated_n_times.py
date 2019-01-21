class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        buffer_set = set()

        for x in A:
            if x not in buffer_set:
                buffer_set.add(x)
            else:
                return x

        return None
