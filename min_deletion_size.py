class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # result_set = set()
        max_length = len(A[0])
        result = 0

        for i in range(max_length):
            col = [a[i] for a in A]

            if col != sorted(col):
                result += 1

        return result

if __name__ == '__main__':
    s = Solution()

    A = ["cba","daf","ghi"]
    # A = ["a","b"]
    # A = ["zyx","wvu","tsr"]
    # A = ["aihdtcw","hqlcusg","ptxfoxq"]
    print(s.minDeletionSize(A))
    # print(s.is_sorted(B))
    # print(s.is_sorted(C))
