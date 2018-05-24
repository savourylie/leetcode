class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        valid_points = [i for i, x in enumerate(s[:-1]) if s[i] != s[i+1]]
        result_count = 0

        for idx in valid_points:
            prev = s[idx]
            mx = min(idx + 2, len_s - idx)
            for i in range(1, mx):
                if s[idx - i + 1] != s[idx + i] and s[idx - i + 1] == prev:
                    result_count += 1
                    prev = s[idx - i + 1]
                else:
                    break

        return result_count
