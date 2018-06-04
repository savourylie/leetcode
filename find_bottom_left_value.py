# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.left_most = [0, 0]
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.left_most[0] = root.val

        _ = self.dfs(root)
        
        return self.left_most[0]
    
    def dfs(self, root, level=0):
        if not root:
            return 
        
        if level > self.left_most[1]:
            self.left_most[0], self.left_most[1] = root.val, level
                
        _ = self.dfs(root.left, level=level+1)
        _ = self.dfs(root.right, level=level+1)