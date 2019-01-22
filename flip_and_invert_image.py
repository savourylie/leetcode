class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows = len(A)
        num_cols = len(A[0])

        B = [[None] * num_cols for _ in range(num_rows)]

        i = 0
        j = num_cols
        v = 0

        while i < num_rows:
            while j > 0:
                element = A[i][j - 1]

                if element == 0:
                    B[i][v] = 1
                else:
                    B[i][v] = 0

                v += 1
                j -= 1

            v = 0
            j = num_cols
            i += 1

        return B

if __name__ == '__main__':
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

    s = Solution()

    print(A)
    print(s.flipAndInvertImage(A))