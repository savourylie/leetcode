# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root, current_height=0):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
		    return current_height

        current_height += 1
    	current_height = max(self.maxDepth(root.left, current_height), self.maxDepth(root.right, current_height))

    	return current_height