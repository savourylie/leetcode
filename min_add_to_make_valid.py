class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """


        num_need = 0
        left_count = 0

        for s in S:
            if s == '(':
                left_count += 1

            elif s == ')':
                if left_count > 0:
                    left_count -= 1
                else:
                    num_need += 1

        return left_count + num_need


if __name__ == '__main__':
    S = "()"
    s = Solution()

    print(s.minAddToMakeValid(S))
    