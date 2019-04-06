class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0

        if x > y:
            x, y = y, x

        x_bin = self._int2binary(x)
        y_bin = self._int2binary(y)

        diff = 0
        last_pos = 0

        for i, digit in enumerate(x_bin):
            if x_bin[i] != y_bin[i]:
                diff += 1

            last_pos = i

        return diff + sum(y_bin[last_pos + 1:])

    @staticmethod
    def _int2binary(x):

        bin_list = []
        quo = x

        while quo:
            quo, res = divmod(quo, 2)
            bin_list.append(res)

        return bin_list if bin_list else [0]


if __name__ == '__main__':
    s = Solution()
    # print(s.hammingDistance(1, 4))
    print(s._int2binary(0))
    print(s._int2binary(1))