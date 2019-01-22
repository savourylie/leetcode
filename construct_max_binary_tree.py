class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        argmax, mx = self.get_argmax(nums)

        root = TreeNode(mx)
        root.left = self.constructMaximumBinaryTree(nums[:argmax])
        root.right = self.constructMaximumBinaryTree(nums[argmax + 1:])

        return root

    @staticmethod
    def get_argmax(nums):
        current_argmax = 0
        current_max = nums[0]

        for i, num in enumerate(nums):
            if num > current_max:
                current_max = num
                current_argmax = i

        return current_argmax, current_max


if __name__ == '__main__':
    nums = [3,2,1,6,0,5]
    s = Solution()
    root = s.constructMaximumBinaryTree(nums)

    print(root.val)