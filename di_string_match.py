class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        i, d = 0, N

        result_list = []

        for s in S:
            if s == 'I':
                result_list.append(i)
                i += 1
            elif s == 'D':
                result_list.append(d)
                d -= 1

        result_list.append(i)

        return result_list



if __name__ == '__main__':
    S = 'IDID'
    # S = 'III'
    # S = 'DDI'
    s = Solution()

    print(s.diStringMatch(S))
