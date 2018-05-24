# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def tree_sum(root):
            if not root:
                return 0
            
            return root.val + tree_sum(root.left) + tree_sum(root.right)
        
        def dfs_change(root, res=0):
            if not root:
                return None
            
            root.val = root.val + tree_sum(root.right) + res
            dfs_change(root.left, root.val)
            dfs_change(root.right, res)
            
            return None
        
        _ = dfs_change(root)
        
        return root