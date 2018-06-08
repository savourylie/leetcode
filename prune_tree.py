# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def tree_sum(root):
            if not root:
                return 0
            
            result = root.val
            result += tree_sum(root.left) + tree_sum(root.right)
            
            return result
        
        def prune_tree(root):
            if not root:
                return None
            
            if tree_sum(root.left) == 0:
                root.left = None
            if tree_sum(root.right) == 0:
                root.right = None
                
            _ = prune_tree(root.left)
            _ = prune_tree(root.right)
            
            return root
            
        return prune_tree(root)