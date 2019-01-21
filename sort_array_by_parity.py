class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_list = []
        odd_list = []

        for x in A:
            if x % 2 == 0:
                even_list.append(x)
            else:
                odd_list.append(x)

        return even_list + odd_list
