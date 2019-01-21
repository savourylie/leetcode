class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_squares = [x**2 for x in A]

        return sorted(A_squares)