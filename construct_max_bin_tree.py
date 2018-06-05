# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def construct_max_bin_tree(nums):
            if not nums:
                return None
            
            i, mx = max(enumerate(nums), key=lambda x:x[1])
            
            root = TreeNode(mx)
            root.left = construct_max_bin_tree(nums[:i])
            root.right = construct_max_bin_tree(nums[i+1:])
            
            return root
            
        return construct_max_bin_tree(nums)
    