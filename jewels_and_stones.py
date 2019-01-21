class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # jewel_set = set(J)
        # counter = 0
        #
        # for i, x in enumerate(S):
        #     if x in jewel_set:
        #         counter += 1
        #
        # return counter

        J_set = set(J)

        counter = 0

        for x in S:
            if x in J_set:
                counter += 1

        return counter


if __name__ == '__main__':
    J = 'aA'
    S = 'aAAbbbb'

    s = Solution()
    result = s.numJewelsInStones(J, S)
    print(result)