class Solution:
    def twoSum(self, nums, target):
        """Use a hash map to save the partner number and the index.
        This way you only have to go one-pass to find the pair.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        partner_dict = {}

        for i, x in enumerate(nums):
            if x in partner_dict:
                return partner_dict[x], i
            else:
                partner_dict[target - x] = i

        return None


if __name__ == '__main__':
    target = 9
    nums = [2, 7, 11, 5]

    s = Solution()
    result = s.twoSum(nums, target)

    print(result)